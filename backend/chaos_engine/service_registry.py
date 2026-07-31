"""
Defines the simulated production services.
"""

from dataclasses import dataclass


@dataclass
class Service:
    """Represents a simulated microservice."""

    name: str
    owner: str
    criticality: str


SERVICES = [
    Service(
        name="Authentication Service",
        owner="Identity Team",
        criticality="HIGH",
    ),
    Service(
        name="Payment Service",
        owner="Finance Team",
        criticality="CRITICAL",
    ),
    Service(
        name="Inventory Service",
        owner="Commerce Team",
        criticality="HIGH",
    ),
    Service(
        name="Notification Service",
        owner="Platform Team",
        criticality="MEDIUM",
    ),
    Service(
        name="Recommendation Service",
        owner="AI Team",
        criticality="MEDIUM",
    ),
]
