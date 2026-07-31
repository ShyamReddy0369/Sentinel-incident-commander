"""Fault injection primitives for the chaos engine."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .metrics import MetricsCollector
from .service_registry import ServiceRegistry


class FaultInjector:
    """Inject faults into registered services and report them."""

    def __init__(self, service_registry: Optional[ServiceRegistry] = None, metrics: Optional[MetricsCollector] = None) -> None:
        self.service_registry = service_registry or ServiceRegistry()
        self.metrics = metrics or MetricsCollector()

    def inject(self, service_name: str, fault_type: str) -> Dict[str, Any]:
        if not self.service_registry.get_service(service_name):
            raise KeyError(f"Unknown service: {service_name}")

        self.metrics.increment("faults_injected")
        self.metrics.record_event(
            "fault_injected", {"service": service_name, "fault_type": fault_type})
        return {"service": service_name, "fault_type": fault_type, "status": "injected"}

    def inject_many(self, fault_types: List[str]) -> List[Dict[str, Any]]:
        results: List[Dict[str, Any]] = []
        for service_name in self.service_registry.list_services():
            for fault_type in fault_types:
                results.append(self.inject(service_name, fault_type))
        return results
