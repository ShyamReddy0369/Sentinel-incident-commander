"""SQL query templates for the incident command system."""

from __future__ import annotations

QUERIES = {
    "healthcheck": "SELECT 1 FROM dual",
    "list_incidents": "SELECT id, title, severity FROM incidents ORDER BY created_at DESC",
}
