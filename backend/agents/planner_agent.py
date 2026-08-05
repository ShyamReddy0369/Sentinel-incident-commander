"""
Planner Agent for Sentinel AI Ops.

Creates an execution plan from the
Diagnosis Agent's output.
"""

from backend.agents.base_agent import BaseAgent


class PlannerAgent(BaseAgent):

    def __init__(self):

        super().__init__("Planner Agent")

    def run(self, diagnosis):

        root_cause = diagnosis["root_cause"]

        if "CPU" in root_cause:

            steps = [
                "Restart the affected service.",
                "Scale service replicas if available.",
                "Terminate CPU-intensive background processes.",
                "Monitor CPU usage for the next 5 minutes.",
                "Close the incident if CPU usage returns to normal.",
            ]

        elif "Memory" in root_cause:

            steps = [
                "Capture a memory dump.",
                "Restart the affected service.",
                "Monitor memory usage.",
                "Investigate possible memory leaks.",
                "Close the incident after validation.",
            ]

        elif "latency" in root_cause.lower():

            steps = [
                "Check upstream services.",
                "Verify database response time.",
                "Inspect network latency.",
                "Continue monitoring until latency stabilizes.",
            ]

        else:

            steps = [
                "Collect additional telemetry.",
                "Escalate to the operations team.",
            ]

        return {
            "agent": self.name,
            "status": "SUCCESS",
            "steps": steps,
        }
