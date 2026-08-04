"""
In-memory repository implementation.
"""

from backend.repository.base import IncidentRepository


class MemoryIncidentRepository(IncidentRepository):

    def __init__(self):
        self.incidents = []

    def save(self, incident):
        self.incidents.append(incident)

    def resolve(self, incident_id):

        for incident in self.incidents:

            if incident.incident_id == incident_id:
                incident.status = "RESOLVED"
                return incident

        return None

    def get_all(self):
        return self.incidents

    def get_open(self):

        return [
            incident
            for incident in self.incidents
            if incident.status == "OPEN"
        ]
