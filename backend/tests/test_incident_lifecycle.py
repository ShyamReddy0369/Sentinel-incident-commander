from backend.chaos_engine.incident_service import IncidentService

service = IncidentService()

incident = service.create_incident(
    "Authentication Service",
    "CRITICAL",
    "CPU exceeded 95%"
)

print(incident)

duplicate = service.create_incident(
    "Authentication Service",
    "CRITICAL",
    "Another CPU spike"
)

print("Duplicate:", duplicate)

resolved = service.resolve_incident("Authentication Service")

print(resolved)

print(service.active_incidents)
