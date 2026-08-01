"""
Telemetry generation for simulated services.

This module is responsible for producing realistic system metrics
that evolve gradually over time.
"""

from __future__ import annotations

import random

from chaos_engine.models import ServiceMetrics


class TelemetryGenerator:
    """
    Generates realistic telemetry for a simulated service.
    """

    def __init__(self) -> None:
        self._metrics = ServiceMetrics(
            cpu_usage=random.uniform(15, 35),
            memory_usage=random.uniform(30, 55),
            disk_usage=random.uniform(20, 45),
            latency_ms=random.randint(20, 80),
            requests_per_second=random.randint(80, 250),
            error_rate=round(random.uniform(0.0, 0.4), 2),
            active_connections=random.randint(5, 30),
        )

    @property
    def metrics(self) -> ServiceMetrics:
        return self._metrics

    def update(self) -> ServiceMetrics:
        """
        Simulate one telemetry update.
        """

        self._metrics.cpu_usage = self._bounded(
            self._metrics.cpu_usage + random.uniform(-3, 3),
            0,
            100,
        )

        self._metrics.memory_usage = self._bounded(
            self._metrics.memory_usage + random.uniform(-2, 2),
            0,
            100,
        )

        self._metrics.disk_usage = self._bounded(
            self._metrics.disk_usage + random.uniform(-0.2, 0.2),
            0,
            100,
        )

        self._metrics.latency_ms = int(
            self._bounded(
                self._metrics.latency_ms + random.randint(-5, 5),
                1,
                5000,
            )
        )

        self._metrics.requests_per_second = int(
            self._bounded(
                self._metrics.requests_per_second
                + random.randint(-20, 20),
                0,
                10000,
            )
        )

        self._metrics.error_rate = round(
            self._bounded(
                self._metrics.error_rate
                + random.uniform(-0.05, 0.05),
                0,
                100,
            ),
            2,
        )

        self._metrics.active_connections = int(
            self._bounded(
                self._metrics.active_connections
                + random.randint(-2, 2),
                0,
                1000,
            )
        )

        return self._metrics

    @staticmethod
    def _bounded(value: float, minimum: float, maximum: float) -> float:
        return max(minimum, min(maximum, value))
