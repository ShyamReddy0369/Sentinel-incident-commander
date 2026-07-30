"""High-level orchestration for the chaos simulator."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .fault_injector import FaultInjector
from .incident_service import IncidentService
from .metrics import MetricsCollector
from .scheduler import Scheduler
from .service_registry import ServiceRegistry
from .utils import utcnow


class ChaosSimulator:
    """Coordinate scheduling, fault injection, and incident tracking."""

    def __init__(
        self,
        service_registry: Optional[ServiceRegistry] = None,
        metrics: Optional[MetricsCollector] = None,
        incident_service: Optional[IncidentService] = None,
    ) -> None:
        self.service_registry = service_registry or ServiceRegistry()
        self.metrics = metrics or MetricsCollector()
        self.incident_service = incident_service or IncidentService(
            self.metrics)
        self.scheduler = Scheduler()
        self.fault_injector = FaultInjector(
            self.service_registry, self.metrics)

    def run(self, duration_seconds: int = 60) -> Dict[str, Any]:
        """Run a short simulation cycle and collect summary data."""
        self.metrics.record_event("simulator_started", {
                                  "started_at": utcnow(), "duration_seconds": duration_seconds})

        for service_name in self.service_registry.list_services():
            self.service_registry.heartbeat(service_name)

        self.scheduler.add_task("inject_faults", lambda: self.fault_injector.inject_many(
            ["latency", "resource_pressure"]), 5)
        self.scheduler.run(iterations=1)

        incident = self.incident_service.create_incident(
            title="Chaos simulation completed",
            severity="medium",
            details={"duration_seconds": duration_seconds,
                     "timestamp": utcnow()},
        )

        return {
            "incident_id": incident["id"],
            "services": self.service_registry.list_services(),
            "metrics": self.metrics.snapshot(),
            "completed_at": utcnow(),
        }
