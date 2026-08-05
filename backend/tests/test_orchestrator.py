"""
Agent Orchestrator test.
"""

from backend.agents.orchestrator import AgentOrchestrator
from backend.chaos_engine.models import Incident


incident = Incident(
    incident_id="INC-000001",
    service_name="Authentication Service",
    severity="CRITICAL",
    description="CPU utilization exceeded 95%",
)

orchestrator = AgentOrchestrator()

report = orchestrator.process_incident(incident)

print("=" * 60)
print("SENTINEL AI ANALYSIS REPORT")
print("=" * 60)

print(f"Incident ID : {report.incident_id}")
print(f"Service     : {report.service_name}")
print(f"Severity    : {report.severity}")

print("\nROOT CAUSE")
print("-" * 60)
print(report.diagnosis["root_cause"])

print("\nPLAN")
print("-" * 60)

for i, step in enumerate(report.execution_plan["steps"], start=1):
    print(f"{i}. {step}")

print("\nREMEDIATION")
print("-" * 60)

for action in report.remediation["completed_actions"]:
    print(f"✔ {action['action']}")

print("\nSUMMARY")
print("-" * 60)
print(report.remediation["summary"])
