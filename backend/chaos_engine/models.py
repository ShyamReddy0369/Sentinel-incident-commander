"""
Domain models used by the Chaos Engine.

These classes represent the state of our simulated
production infrastructure.

Nothing in this file should contain business logic.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class ServiceMetrics:
    """
    Represents the current telemetry of one service.
    """

    cpu_usage: float
    memory_usage: float
    disk_usage: float

    latency_ms: int

    requests_per_second: int

    error_rate: float

    active_connections: int

    updated_at: datetime = field(default_factory=datetime.utcnow)


@dataclass(slots=True)
class ServiceState:
    """
    Represents one simulated microservice.
    """

    name: str

    owner: str

    criticality: str

    metrics: ServiceMetrics

    health_status: str = "HEALTHY"
