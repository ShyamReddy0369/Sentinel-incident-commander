"""
Incident Detection and Lifecycle Manager.
"""

from __future__ import annotations

from backend.chaos_engine.models import Incident
from backend.repository import MemoryIncidentRepository


class IncidentService:
    """
    Manages the lifecycle of incidents.

    Responsibilities:
    - Create incidents
    - Prevent duplicate incidents
    - Resolve incidents
    - Store incident history using the repository
    """

    def __init__(self):

        self._next_id = 1

        # Active incidents indexed by service name
        self.active_incidents = {}

        # Persistent repository (memory today, Oracle later)
        self.repository = MemoryIncidentRepository()

    def create_incident(
        self,
        service_name: str,
        severity: str,
        description: str,
    ) -> Incident | None:

        # Prevent duplicate incidents
        if service_name in self.active_incidents:
            return None

        incident = Incident(
            incident_id=self._generate_id(),
            service_name=service_name,
            severity=severity,
            description=description,
        )

        self.active_incidents[service_name] = incident

        # Save incident history
        self.repository.save(incident)

        return incident

    def resolve_incident(self, service_name: str):

        if service_name not in self.active_incidents:
            return None

        incident = self.active_incidents[service_name]

        incident.status = "RESOLVED"

        # Update repository
        self.repository.resolve(incident.incident_id)

        del self.active_incidents[service_name]

        return incident

    def get_all_incidents(self):
        return self.repository.get_all()

    def get_open_incidents(self):
        return self.repository.get_open()

    def _generate_id(self) -> str:

        incident_id = f"INC-{self._next_id:06d}"

        self._next_id += 1

        return incident_id
