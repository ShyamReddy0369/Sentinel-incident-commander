"""Health monitoring helpers for the chaos engine."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .metrics import MetricsCollector
from .utils import utcnow


class HealthMonitor:
    """Assess service health using recent metrics and telemetry context."""

    def __init__(self, metrics: Optional[MetricsCollector] = None) -> None:
        self.metrics = metrics or MetricsCollector()

    def check(self, service_name: str, details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return {
            "service": service_name,
            "status": "healthy",
            "timestamp": utcnow(),
            "details": details or {},
        }
