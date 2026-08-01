"""Telemetry helpers for the chaos engine."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .utils import utcnow


class TelemetryCollector:
    """Collect structured telemetry events emitted during simulations."""

    def __init__(self) -> None:
        self._events: list[Dict[str, Any]] = []

    def record(self, event_type: str, payload: Optional[Dict[str, Any]] = None) -> None:
        self._events.append(
            {
                "type": event_type,
                "timestamp": utcnow(),
                "payload": payload or {},
            }
        )

    def snapshot(self) -> Dict[str, Any]:
        return {"events": list(self._events)}
