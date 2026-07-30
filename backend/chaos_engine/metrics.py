"""Lightweight metrics collection helpers."""

from __future__ import annotations

from typing import Any, Dict


class MetricsCollector:
    """Collect counters and event data for the chaos engine."""

    def __init__(self) -> None:
        self._counters: Dict[str, int] = {}
        self._events: list[Dict[str, Any]] = []

    def increment(self, name: str, value: int = 1) -> None:
        self._counters[name] = self._counters.get(name, 0) + value

    def record_event(self, event_type: str, payload: Dict[str, Any] | None = None) -> None:
        self._events.append({"type": event_type, "payload": payload or {}})

    def snapshot(self) -> Dict[str, Any]:
        return {"counters": dict(self._counters), "events": list(self._events)}
