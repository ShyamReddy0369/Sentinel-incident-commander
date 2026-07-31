"""Helpers for generating synthetic fault and incident payloads."""

from __future__ import annotations

from random import choice
from typing import Any, Dict, List

from .utils import utcnow


def generate_faults(service_names: List[str], count: int = 3) -> List[Dict[str, Any]]:
    """Generate a list of synthetic fault descriptors."""
    fault_types = ["latency", "resource_pressure", "packet_loss", "crash"]
    faults: List[Dict[str, Any]] = []
    for _ in range(min(count, len(service_names))):
        service_name = choice(service_names)
        faults.append({"service": service_name, "fault_type": choice(
            fault_types), "timestamp": utcnow()})
    return faults


def generate_incident_template() -> Dict[str, Any]:
    """Create a basic incident template for downstream services."""
    return {
        "title": "Synthetic incident",
        "severity": "medium",
        "details": {"created_at": utcnow()},
    }
