"""
Health evaluation engine for Sentinel AI Ops.
"""

from backend.chaos_engine.models import ServiceMetrics


class HealthEngine:

    def evaluate(self, metrics: ServiceMetrics) -> str:
        """
        Evaluates the health of a service based on
        CPU, memory, latency, and error rate.

        NOTE:
        These thresholds are intentionally lowered
        for development/demo purposes so incidents
        occur frequently enough to test the AI pipeline.
        """

        # ------------------------
        # CRITICAL
        # ------------------------

        if (
            metrics.cpu_usage >= 90
            or metrics.memory_usage >= 90
            or metrics.error_rate >= 5
            or metrics.latency_ms >= 500
        ):
            return "CRITICAL"

        # ------------------------
        # WARNING
        # ------------------------

        if (
            metrics.cpu_usage >= 60
            or metrics.memory_usage >= 60
            or metrics.error_rate >= 1
            or metrics.latency_ms >= 120
        ):
            return "WARNING"

        # ------------------------
        # HEALTHY
        # ------------------------

        return "HEALTHY"
