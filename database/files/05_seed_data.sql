-- Sentinel -- Autonomous Incident Commander
-- Phase 1e: Seed data
-- Run after 04_views.sql. Safe to re-run after TRUNCATE if you want a
-- clean slate later.

INSERT INTO services (name, description) VALUES
    ('auth-service', 'Handles user authentication and session tokens');
INSERT INTO services (name, description) VALUES
    ('payments-service', 'Processes payment transactions');
INSERT INTO services (name, description) VALUES
    ('orders-service', 'Manages order creation and fulfillment');
INSERT INTO services (name, description) VALUES
    ('notifications-service', 'Sends email and SMS notifications');

INSERT INTO runbooks (fault_signature, title, remediation_steps, risk_level) VALUES
    ('MEMORY_LEAK', 'Service memory leak',
     'Restart the affected service pod; if it recurs within 1 hour, roll back the last deploy.',
     'LOW');
INSERT INTO runbooks (fault_signature, title, remediation_steps, risk_level) VALUES
    ('DEPLOY_REGRESSION', 'Bad deploy causing error spike',
     'Roll back to the previous stable release tag immediately.',
     'HIGH');
INSERT INTO runbooks (fault_signature, title, remediation_steps, risk_level) VALUES
    ('DB_POOL_EXHAUSTION', 'Database connection pool exhausted',
     'Temporarily increase pool size and restart the service; investigate the connection leak.',
     'MEDIUM');

COMMIT;
