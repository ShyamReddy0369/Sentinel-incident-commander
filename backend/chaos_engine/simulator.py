"""
Digital Infrastructure Simulator.

This module ties together the telemetry generator,
fault injector, and health engine.
"""

from __future__ import annotations

import random
import time

from backend.chaos_engine.telemetry import TelemetryGenerator
from backend.chaos_engine.health import HealthEngine
from backend.chaos_engine.fault_injector import (
    CPUSpikeFault,
    MemoryLeakFault,
)


SERVICES = [
    "Authentication Service",
    "Payment Service",
    "Inventory Service",
]


class Simulator:

    def __init__(self):

        self.health_engine = HealthEngine()

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

            time.sleep(1)


if __name__ == "__main__":

    simulator = Simulator()

    simulator.run()
