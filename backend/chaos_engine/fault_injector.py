"""
Fault Injection Engine for Sentinel AI Ops.

This module simulates realistic production failures by
modifying service telemetry instead of directly creating
incidents.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from backend.chaos_engine.models import ServiceMetrics


class Fault(ABC):
    """
    Base class for all simulated faults.
    """

    name: str = "Generic Fault"

    @abstractmethod
    def apply(self, metrics: ServiceMetrics) -> None:
        """
        Apply this fault to the provided metrics.
        """
        pass


class CPUSpikeFault(Fault):
    """
    Simulates a sudden CPU spike.
    """

    name = "CPU Spike"

    def apply(self, metrics: ServiceMetrics) -> None:

        metrics.cpu_usage = min(metrics.cpu_usage + 25, 100)

        metrics.latency_ms += 40

        metrics.error_rate += 0.4


class MemoryLeakFault(Fault):
    """
    Simulates a gradual memory leak.
    """

    name = "Memory Leak"

    def apply(self, metrics: ServiceMetrics) -> None:

        metrics.memory_usage = min(metrics.memory_usage + 12, 100)

        metrics.latency_ms += 15

        metrics.error_rate += 0.1
