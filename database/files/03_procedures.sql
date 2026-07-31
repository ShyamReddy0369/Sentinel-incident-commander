-- Sentinel -- Autonomous Incident Commander
-- Phase 1c: pkg_incident_mgmt package
-- Run after 02_triggers.sql.

CREATE OR REPLACE PACKAGE pkg_incident_mgmt AS

    -- Moves an incident to a new status, enforcing the state machine
    -- below. Raises ORA-20001 if the transition isn't allowed.
    --   OPEN              -> DIAGNOSING
    --   DIAGNOSING        -> AWAITING_APPROVAL | REMEDIATING
    --   AWAITING_APPROVAL -> REMEDIATING | DIAGNOSING
    --   REMEDIATING       -> MONITORING
    --   MONITORING        -> RESOLVED | DIAGNOSING   (regression reopens)
    PROCEDURE sp_transition_status(
        p_incident_id   IN incidents.id%TYPE,
        p_new_status    IN incidents.status%TYPE
    );

    -- Minutes between started_at and resolved_at. NULL if not yet resolved.
    FUNCTION fn_mttr_minutes(
        p_incident_id   IN incidents.id%TYPE
    ) RETURN NUMBER;

    -- Convenience wrapper so agents can drop a note into an incident's
    -- timeline without knowing the incident_events table structure.
    PROCEDURE sp_log_event(
        p_incident_id   IN incidents.id%TYPE,
        p_event_type    IN VARCHAR2,
        p_agent_name    IN VARCHAR2,
        p_message       IN VARCHAR2
    );

END pkg_incident_mgmt;
/

CREATE OR REPLACE PACKAGE BODY pkg_incident_mgmt AS

    PROCEDURE sp_transition_status(
        p_incident_id   IN incidents.id%TYPE,
        p_new_status    IN incidents.status%TYPE
    ) IS
        v_current_status    incidents.status%TYPE;
        v_valid             BOOLEAN := FALSE;
    BEGIN
        -- FOR UPDATE locks this row until the caller commits or rolls
        -- back. Without it, two agents transitioning the same incident
        -- at once could both read the same "current" status and both
        -- succeed, corrupting the state machine -- a race condition
        -- that only shows up under real concurrent load.
        SELECT status INTO v_current_status
        FROM incidents
        WHERE id = p_incident_id
        FOR UPDATE;

        -- The allowed-transitions map. Anything not listed here is
        -- rejected -- this CASE block *is* the state machine.
        CASE v_current_status
            WHEN 'OPEN' THEN
                v_valid := p_new_status = 'DIAGNOSING';
            WHEN 'DIAGNOSING' THEN
                v_valid := p_new_status IN ('AWAITING_APPROVAL', 'REMEDIATING');
            WHEN 'AWAITING_APPROVAL' THEN
                v_valid := p_new_status IN ('REMEDIATING', 'DIAGNOSING');
            WHEN 'REMEDIATING' THEN
                v_valid := p_new_status = 'MONITORING';
            WHEN 'MONITORING' THEN
                v_valid := p_new_status IN ('RESOLVED', 'DIAGNOSING');
            ELSE
                v_valid := FALSE;
        END CASE;

        IF NOT v_valid THEN
            RAISE_APPLICATION_ERROR(
                -20001,
                'Invalid transition: ' || v_current_status || ' -> ' || p_new_status
            );
        END IF;

        UPDATE incidents
        SET status = p_new_status
        WHERE id = p_incident_id;

        -- Deliberately no COMMIT here. A reusable procedure shouldn't
        -- decide the transaction boundary for its caller -- Flask (via
        -- the Python DB driver) owns that decision.
    END sp_transition_status;


    FUNCTION fn_mttr_minutes(
        p_incident_id   IN incidents.id%TYPE
    ) RETURN NUMBER IS
        v_started   incidents.started_at%TYPE;
        v_resolved  incidents.resolved_at%TYPE;
        v_diff      INTERVAL DAY TO SECOND;
    BEGIN
        SELECT started_at, resolved_at INTO v_started, v_resolved
        FROM incidents
        WHERE id = p_incident_id;

        IF v_resolved IS NULL THEN
            RETURN NULL;
        END IF;

        -- Subtracting two TIMESTAMPs returns an INTERVAL DAY TO SECOND,
        -- not a plain number -- that shortcut only works with DATE.
        -- EXTRACT pulls each component back out so we can add them up
        -- as minutes.
        v_diff := v_resolved - v_started;

        RETURN ROUND(
            EXTRACT(DAY    FROM v_diff) * 24 * 60 +
            EXTRACT(HOUR   FROM v_diff) * 60 +
            EXTRACT(MINUTE FROM v_diff) +
            EXTRACT(SECOND FROM v_diff) / 60
        , 1);
    END fn_mttr_minutes;


    PROCEDURE sp_log_event(
        p_incident_id   IN incidents.id%TYPE,
        p_event_type    IN VARCHAR2,
        p_agent_name    IN VARCHAR2,
        p_message       IN VARCHAR2
    ) IS
    BEGIN
        INSERT INTO incident_events (incident_id, event_type, agent_name, message)
        VALUES (p_incident_id, p_event_type, p_agent_name, p_message);
    END sp_log_event;

END pkg_incident_mgmt;
/
