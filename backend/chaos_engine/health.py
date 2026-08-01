"""
Health evaluation engine for Sentinel AI Ops.
"""

from backend.chaos_engine.models import ServiceMetrics


class HealthEngine:
    def evaluate(self, metrics: ServiceMetrics) -> str:

        if (
            metrics.cpu_usage >= 95
            or metrics.memory_usage >= 95
            or metrics.error_rate >= 10
            or metrics.latency_ms >= 800
        ):
            return "CRITICAL"

        if (
            metrics.cpu_usage >= 80
            or metrics.memory_usage >= 80
            or metrics.error_rate >= 2
            or metrics.latency_ms >= 250
        ):
            return "WARNING"

        return "HEALTHY"
