from backend.chaos_engine.incident_service import IncidentService

service = IncidentService()

incident = service.create_incident(
    service_name="Authentication Service",
    severity="CRITICAL",
    description="CPU utilization exceeded 95%"
)

print("=" * 50)

print("Incident Created")

print(f"ID          : {incident.incident_id}")
print(f"Service     : {incident.service_name}")
print(f"Severity    : {incident.severity}")
print(f"Status      : {incident.status}")
print(f"Description : {incident.description}")
print(f"Created At  : {incident.created_at}")
