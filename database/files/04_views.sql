-- Sentinel -- Autonomous Incident Commander
-- Phase 1d: Reporting views
-- Run after 03_procedures.sql.

-- Feeds the Streamlit ops dashboard (Phase 6) directly -- one query,
-- no app-side aggregation needed.
CREATE OR REPLACE VIEW vw_incident_dashboard_summary AS
SELECT
    COUNT(*)                                                   AS total_incidents,
    SUM(CASE WHEN status != 'RESOLVED' THEN 1 ELSE 0 END)      AS open_incidents,
    SUM(CASE WHEN status = 'RESOLVED' THEN 1 ELSE 0 END)       AS resolved_incidents,
    SUM(CASE WHEN severity = 'CRITICAL' THEN 1 ELSE 0 END)     AS critical_count,
    SUM(CASE WHEN severity = 'HIGH' THEN 1 ELSE 0 END)         AS high_count,
    ROUND(AVG(
        CASE WHEN resolved_at IS NOT NULL
             THEN pkg_incident_mgmt.fn_mttr_minutes(id)
        END
    ), 1)                                                       AS avg_mttr_minutes
FROM incidents;

-- Feeds the incident detail page in Mission Control (Phase 5) -- the
-- full chronological story of one incident in a single query.
CREATE OR REPLACE VIEW vw_incident_timeline AS
SELECT
    ie.incident_id,
    i.incident_number,
    ie.event_type,
    ie.agent_name,
    ie.message,
    ie.created_at
FROM incident_events ie
JOIN incidents i ON i.id = ie.incident_id;
-- Note: callers should still add their own ORDER BY created_at --
-- Oracle doesn't guarantee a view's internal ordering survives once
-- the view is queried through further joins or filters.

-- Feeds the human approval queue in Mission Control -- every
-- high-risk action still waiting on a decision.
CREATE OR REPLACE VIEW vw_pending_approvals AS
SELECT
    ap.id                  AS approval_id,
    aa.id                  AS agent_action_id,
    aa.incident_id,
    i.incident_number,
    aa.agent_name,
    aa.action_type,
    aa.target_service,
    aa.risk_level,
    ap.requested_at
FROM approvals ap
JOIN agent_actions aa ON aa.id = ap.agent_action_id
JOIN incidents i ON i.id = aa.incident_id
WHERE ap.decision IS NULL;
