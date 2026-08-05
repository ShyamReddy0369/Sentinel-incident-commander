"""
Agent Orchestrator for Sentinel AI Ops.

Coordinates all AI agents.
"""

from backend.agents.diagnosis_agent import DiagnosisAgent
from backend.agents.models import AnalysisReport
from backend.agents.planner_agent import PlannerAgent
from backend.agents.remediation_agent import RemediationAgent


class AgentOrchestrator:

    def __init__(self):

        self.diagnosis_agent = DiagnosisAgent()
        self.planner_agent = PlannerAgent()
        self.remediation_agent = RemediationAgent()

    def process_incident(self, incident):

        diagnosis = self.diagnosis_agent.run(incident)

        plan = self.planner_agent.run(diagnosis)

        remediation = self.remediation_agent.run(plan)

        return AnalysisReport(
            incident_id=incident.incident_id,
            service_name=incident.service_name,
            severity=incident.severity,
            diagnosis=diagnosis,
            execution_plan=plan,
            remediation=remediation,
        )
