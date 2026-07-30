"""Service registration utilities for the chaos engine."""

from __future__ import annotations

from typing import Dict, List, Optional


class ServiceRegistry:
    """Track simulated services and their state."""

    def __init__(self) -> None:
        self._services: Dict[str, Dict[str, object]] = {}

    def register(self, name: str, metadata: Optional[Dict[str, object]] = None) -> None:
        self._services[name] = {"name": name, **(metadata or {})}

    def get_service(self, name: str) -> Optional[Dict[str, object]]:
        return self._services.get(name)

    def list_services(self) -> List[str]:
        return list(self._services.keys())

    def heartbeat(self, name: str) -> Dict[str, object]:
        service = self.get_service(name)
        if service is None:
            raise KeyError(f"Unknown service: {name}")
        service["last_heartbeat"] = "ok"
        return service
