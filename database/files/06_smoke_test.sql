-- Sentinel -- Autonomous Incident Commander
-- Phase 1f: Smoke test
-- Run these one block at a time and read the comments -- this proves
-- the schema, triggers, and package actually work together before you
-- move on to Phase 2.

-- 1. Create a test incident against auth-service (service id 1 from
--    the seed data). Confirm the trigger auto-generates incident_number.
INSERT INTO incidents (service_id, status, severity, title)
VALUES (1, 'OPEN', 'HIGH', 'auth-service returning intermittent 500s');
COMMIT;

SELECT id, incident_number, status, severity, title FROM incidents;
-- Expect: incident_number = 'INC-0001', status = 'OPEN'


-- 2. Transition it through the state machine using the package
--    procedure -- NOT a raw UPDATE. This should succeed and the audit
--    trigger should log it automatically.
BEGIN
    pkg_incident_mgmt.sp_transition_status(1, 'DIAGNOSING');
END;
/
COMMIT;

SELECT * FROM vw_incident_timeline WHERE incident_id = 1 ORDER BY created_at;
-- Expect one row: "Status changed: OPEN -> DIAGNOSING"


-- 3. Try an INVALID transition -- OPEN incidents that are now
--    DIAGNOSING cannot jump straight to RESOLVED. This should fail
--    with ORA-20001.
BEGIN
    pkg_incident_mgmt.sp_transition_status(1, 'RESOLVED');
END;
/
-- Expect: ORA-20001: Invalid transition: DIAGNOSING -> RESOLVED
-- If this SUCCEEDS instead of erroring, something is wrong -- stop and
-- recheck 03_procedures.sql before continuing.


-- 4. Propose a HIGH-risk action and confirm it auto-queues for
--    approval without any extra code -- that's the safety-boundary
--    trigger doing its job.
INSERT INTO agent_actions (incident_id, runbook_id, agent_name, action_type, target_service, risk_level)
VALUES (1, 2, 'executor_agent', 'ROLLBACK_DEPLOY', 'auth-service', 'HIGH');
COMMIT;

SELECT * FROM vw_pending_approvals;
-- Expect one row: agent_action for ROLLBACK_DEPLOY, awaiting a decision


-- 5. Check the dashboard summary view -- this is exactly what the
--    Streamlit ops dashboard will query in Phase 6.
SELECT * FROM vw_incident_dashboard_summary;
-- Expect: total_incidents = 1, open_incidents = 1, high_count = 1,
--         avg_mttr_minutes = NULL (nothing resolved yet)


-- If all five checks matched, Phase 1 is confirmed working.
