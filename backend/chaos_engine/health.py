"""
Health evaluation engine for Sentinel AI Ops.
"""

from backend.chaos_engine.models import ServiceMetrics


class HealthEngine:

    def evaluate(self, metrics: ServiceMetrics) -> str:

        score = self.health_score(metrics)

        if score >= 70:
            return "CRITICAL"

        if score >= 40:
            return "WARNING"

        return "HEALTHY"

    def health_score(self, metrics: ServiceMetrics) -> int:

        score = 0

        # CPU
        if metrics.cpu_usage >= 90:
            score += 30
        elif metrics.cpu_usage >= 75:
            score += 15

        # Memory
        if metrics.memory_usage >= 90:
            score += 25
        elif metrics.memory_usage >= 75:
            score += 12

        # Latency
        if metrics.latency_ms >= 400:
            score += 20
        elif metrics.latency_ms >= 200:
            score += 10

        # Error Rate
        if metrics.error_rate >= 2:
            score += 25
        elif metrics.error_rate >= 1:
            score += 12

        return score
