"""
Digital Infrastructure Simulator.

This module ties together the telemetry generator,
fault injector, health engine, incident service,
and AI agent orchestrator.
"""

from __future__ import annotations

import random
import time

from backend.agents.orchestrator import AgentOrchestrator
from backend.chaos_engine.fault_injector import (
    CPUSpikeFault,
    MemoryLeakFault,
)
from backend.chaos_engine.health import HealthEngine
from backend.chaos_engine.incident_service import IncidentService
from backend.chaos_engine.telemetry import TelemetryGenerator


SERVICES = [
    "Authentication Service",
    "Payment Service",
    "Inventory Service",
]


class Simulator:

    def __init__(self):

        self.health_engine = HealthEngine()
        self.incident_service = IncidentService()
        self.orchestrator = AgentOrchestrator()

        self.services = {
            service: TelemetryGenerator()
            for service in SERVICES
        }

    def run(self, cycles: int = 20):

        for cycle in range(1, cycles + 1):

            print("=" * 70)
            print(f"Cycle {cycle}")

            for service, telemetry in self.services.items():

                metrics = telemetry.update()

                if random.random() < 0.10:

                    fault = random.choice(
                        [
                            CPUSpikeFault(),
                            MemoryLeakFault(),
                        ]
                    )

                    print(f"\n⚠ Injecting {fault.name} into {service}")

                    fault.apply(metrics)

                health = self.health_engine.evaluate(metrics)

                print(f"\n{service}")
                print(f"CPU        : {metrics.cpu_usage:.1f}%")
                print(f"Memory     : {metrics.memory_usage:.1f}%")
                print(f"Latency    : {metrics.latency_ms} ms")
                print(f"Errors     : {metrics.error_rate:.2f}%")
                print(f"Health     : {health}")

                # -------------------------
                # Incident Creation
                # -------------------------

                if health in ("WARNING", "CRITICAL"):

                    if metrics.cpu_usage >= 60:
                        description = (
                            f"CPU utilization exceeded threshold ({metrics.cpu_usage:.1f}%)."
                        )

                    elif metrics.memory_usage >= 60:
                        description = f"Memory utilization exceeded threshold ({metrics.memory_usage:.1f}%)."

                    elif metrics.latency_ms >= 120:
                        description = f"Latency exceeded threshold ({metrics.latency_ms} ms)."

                    elif metrics.error_rate >= 1:
                        description = f"Error rate exceeded threshold ({metrics.error_rate:.2f}%)."

                    else:
                        description = f"{service} entered {health} state."

                    incident = self.incident_service.create_incident(
                        service_name=service,
                        severity=health,
                        description=description,
                    )

                    if incident:

                        print("\n🚨 INCIDENT CREATED")
                        print(f"ID       : {incident.incident_id}")
                        print(f"Status   : {incident.status}")

                        report = self.orchestrator.process_incident(
                            incident
                        )

                        print("\n================ AI ANALYSIS ================")

                        diagnosis = report["diagnosis"]

                        print("\nROOT CAUSE")
                        print("-" * 50)
                        print(diagnosis["root_cause"])

                        print("\nCONFIDENCE")
                        print("-" * 50)
                        print(f'{diagnosis["confidence"]}%')

                        print("\nEXECUTION PLAN")
                        print("-" * 50)

                        for i, step in enumerate(
                            report["plan"]["steps"],
                            start=1,
                        ):
                            print(f"{i}. {step}")

                        print("\nREMEDIATION")
                        print("-" * 50)

                        for action in report["remediation"]["completed_actions"]:
                            print(f"✔ {action['action']}")

                        print("\nSUMMARY")
                        print("-" * 50)
                        print(report["remediation"]["summary"])

                # -------------------------
                # Incident Resolution
                # -------------------------

                else:

                    incident = self.incident_service.resolve_incident(
                        service
                    )

                    if incident:

                        print(
                            f"\n✅ INCIDENT RESOLVED : "
                            f"{incident.incident_id}"
                        )

            print("\n" + "=" * 70)
            print("ACTIVE INCIDENTS")

            if not self.incident_service.active_incidents:

                print("None")

            else:

                for incident in self.incident_service.active_incidents.values():

                    print(
                        f"{incident.incident_id} | "
                        f"{incident.service_name} | "
                        f"{incident.severity} | "
                        f"{incident.status}"
                    )

            time.sleep(1)


if __name__ == "__main__":

    Simulator().run()
