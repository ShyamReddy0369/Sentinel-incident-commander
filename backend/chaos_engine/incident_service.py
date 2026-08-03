"""
Incident Detection and Management Engine.
"""

from __future__ import annotations

from backend.chaos_engine.models import Incident


class IncidentService:
    """
    Creates and manages incidents detected
    by the Health Engine.
    """

    def __init__(self):

        self._next_id = 1

        self.active_incidents = []

    def create_incident(
        self,
        service_name: str,
        severity: str,
        description: str,
    ) -> Incident:

        incident = Incident(
            incident_id=self._generate_id(),
            service_name=service_name,
            severity=severity,
            description=description,
        )

        self.active_incidents.append(incident)

        return incident

    def _generate_id(self) -> str:

        incident_id = f"INC-{self._next_id:06d}"

        self._next_id += 1

        return incident_id
