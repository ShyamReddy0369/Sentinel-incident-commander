"""Incident tracking helpers for the chaos engine."""

from __future__ import annotations

from typing import Any, Dict, List

from .metrics import MetricsCollector
from .utils import utcnow


class IncidentService:
    """Store and update incident records in memory."""

    def __init__(self, metrics: MetricsCollector | None = None) -> None:
        self._incidents: List[Dict[str, Any]] = []
        self.metrics = metrics or MetricsCollector()

    def create_incident(self, title: str, severity: str, details: Dict[str, Any] | None = None) -> Dict[str, Any]:
        incident = {
            "id": len(self._incidents) + 1,
            "title": title,
            "severity": severity,
            "details": details or {},
            "created_at": utcnow(),
        }
        self._incidents.append(incident)
        self.metrics.increment("incidents_created")
        self.metrics.record_event(
            "incident_created", {"id": incident["id"], "title": title})
        return incident

    def list_incidents(self) -> List[Dict[str, Any]]:
        return list(self._incidents)
