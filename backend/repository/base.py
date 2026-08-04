"""
Base repository interface for Sentinel AI Ops.
"""

from abc import ABC, abstractmethod


class IncidentRepository(ABC):

    @abstractmethod
    def save(self, incident):
        pass

    @abstractmethod
    def resolve(self, incident_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_open(self):
        pass
