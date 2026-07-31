-- Sentinel -- Autonomous Incident Commander
-- Phase 1b: Triggers
-- Run after 01_schema.sql.

-- Generates a human-readable ticket number ("INC-0001") on insert.
-- BEFORE INSERT because we need to set :NEW.incident_number before the
-- row is written -- an AFTER trigger would be too late to change it.
CREATE OR REPLACE TRIGGER trg_incident_number
BEFORE INSERT ON incidents
FOR EACH ROW
BEGIN
    :NEW.incident_number := 'INC-' || LPAD(seq_incident_number.NEXTVAL, 4, '0');
END;
/

-- Auto-stamps resolved_at the moment status flips to RESOLVED.
-- Must be BEFORE, not AFTER: only a BEFORE row-level trigger is allowed
-- to modify :NEW column values before Oracle writes the row to disk.
CREATE OR REPLACE TRIGGER trg_incident_resolved_stamp
BEFORE UPDATE OF status ON incidents
FOR EACH ROW
WHEN (NEW.status = 'RESOLVED' AND OLD.status != 'RESOLVED')
BEGIN
    :NEW.resolved_at := SYSTIMESTAMP;
END;
/

-- Writes every status change to the audit trail automatically, so no
-- caller (Flask, an agent, a manual SQL update) can change an incident's
-- status without it showing up in the timeline. This runs AFTER the
-- update commits to `incidents`, which is safe because it only touches
-- a different table (incident_events).
CREATE OR REPLACE TRIGGER trg_incident_status_audit
AFTER UPDATE OF status ON incidents
FOR EACH ROW
WHEN (NEW.status != OLD.status)
BEGIN
    INSERT INTO incident_events (incident_id, event_type, agent_name, message)
    VALUES (
        :NEW.id,
        'STATUS_CHANGE',
        'system',
        'Status changed: ' || :OLD.status || ' -> ' || :NEW.status
    );
END;
/

-- The safety-boundary trigger: the instant an agent proposes a HIGH-risk
-- action, this fires and creates a pending approval record -- no app
-- code has to remember to do it, and no app-side bug can skip it. This
-- is the database enforcing the autonomy policy, not just Python.
CREATE OR REPLACE TRIGGER trg_high_risk_approval
AFTER INSERT ON agent_actions
FOR EACH ROW
WHEN (NEW.risk_level = 'HIGH')
BEGIN
    INSERT INTO approvals (agent_action_id)
    VALUES (:NEW.id);

    INSERT INTO incident_events (incident_id, event_type, agent_name, message)
    VALUES (
        :NEW.incident_id,
        'APPROVAL_REQUESTED',
        :NEW.agent_name,
        'High-risk action "' || :NEW.action_type || '" queued for human approval'
    );
END;
/
