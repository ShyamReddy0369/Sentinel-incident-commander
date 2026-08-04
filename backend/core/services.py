"""
Shared service instances for Sentinel AI Ops.

Every module imports these objects instead of creating
its own instances.
"""

from backend.chaos_engine.health import HealthEngine
from backend.chaos_engine.incident_service import IncidentService

health_engine = HealthEngine()

incident_service = IncidentService()
