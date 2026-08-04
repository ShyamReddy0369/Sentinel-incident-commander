"""
Diagnosis Agent test.
"""

from backend.agents.diagnosis_agent import DiagnosisAgent
from backend.chaos_engine.models import Incident


incident = Incident(
    incident_id="INC-000001",
    service_name="Authentication Service",
    severity="CRITICAL",
    description="CPU utilization exceeded 95%"
)

agent = DiagnosisAgent()

report = agent.analyze(incident)

print("=" * 60)
print("AI DIAGNOSIS REPORT")
print("=" * 60)

for key, value in report.items():
    print(f"{key:15}: {value}")
