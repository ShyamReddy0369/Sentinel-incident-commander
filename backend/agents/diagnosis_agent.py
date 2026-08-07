"""
Diagnosis Agent for Sentinel AI Ops.

Analyzes incidents and produces a diagnosis
containing the probable root cause,
confidence score, and recommendation.
"""

from backend.agents.base_agent import BaseAgent
from backend.chaos_engine.models import Incident


class DiagnosisAgent(BaseAgent):

    def __init__(self):

        super().__init__("Diagnosis Agent")

    def run(self, incident: Incident):

        return {
            "agent": self.name,
            "status": "SUCCESS",
            "incident_id": incident.incident_id,
            "service_name": incident.service_name,
            "severity": incident.severity,
            "root_cause": self._root_cause(incident),
            "confidence": self._confidence(incident),
            "recommendation": self._recommendation(incident),
        }

    def _root_cause(self, incident: Incident):

        text = incident.description.lower()

        if "cpu" in text:
            return "High CPU utilization caused by a simulated CPU Spike."

        if "memory" in text:
            return "Memory Leak detected causing abnormal memory growth."

        if "latency" in text:
            return "Service latency exceeded acceptable thresholds."

        return "Unknown root cause."

    def _confidence(self, incident: Incident):

        if incident.severity == "CRITICAL":
            return 98

        if incident.severity == "WARNING":
            return 90

        return 75

    def _recommendation(self, incident: Incident):

        text = incident.description.lower()

        if "cpu" in text:
            return (
                "Investigate CPU-intensive processes and "
                "consider restarting the affected service."
            )

        if "memory" in text:
            return (
                "Inspect memory allocation and restart the "
                "service if memory usage continues increasing."
            )

        if "latency" in text:
            return (
                "Check upstream dependencies and network performance."
            )

        return (
            "Collect additional telemetry before taking action."
        )
