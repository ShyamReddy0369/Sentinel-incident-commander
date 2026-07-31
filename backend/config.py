"""
Application configuration for Sentinel Incident Commander.

All configurable values for the backend live here.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ChaosEngineConfig:
    """Configuration for the chaos engine."""

    SIMULATION_INTERVAL_SECONDS: int = 5

    MAX_SERVICES: int = 5

    INCIDENT_PROBABILITY: float = 0.15

    CPU_WARNING_THRESHOLD: int = 80

    CPU_CRITICAL_THRESHOLD: int = 95

    MEMORY_WARNING_THRESHOLD: int = 80

    MEMORY_CRITICAL_THRESHOLD: int = 95

    LATENCY_WARNING_MS: int = 250

    LATENCY_CRITICAL_MS: int = 500


@dataclass(frozen=True)
class LoggingConfig:
    """Logging configuration."""

    LOG_LEVEL: str = "INFO"

    LOG_DIRECTORY: str = "logs"

    LOG_FILE: str = "chaos_engine.log"


chaos_config = ChaosEngineConfig()
logging_config = LoggingConfig()
