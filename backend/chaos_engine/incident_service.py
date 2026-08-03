"""
Incident Detection and Lifecycle Manager.
"""

from backend.chaos_engine.models import Incident


class IncidentService:

    def __init__(self):
        self._next_id = 1
        self.active_incidents = {}

    def create_incident(self, service_name, severity, description):

        if service_name in self.active_incidents:
            return None

        incident = Incident(
            incident_id=self._generate_id(),
            service_name=service_name,
            severity=severity,
            description=description,
        )

        self.active_incidents[service_name] = incident

        return incident

    def resolve_incident(self, service_name):

        if service_name not in self.active_incidents:
            return None

        incident = self.active_incidents[service_name]
        incident.status = "RESOLVED"

        del self.active_incidents[service_name]

        return incident

    def _generate_id(self):

        incident_id = f"INC-{self._next_id:06d}"
        self._next_id += 1
        return incident_id
