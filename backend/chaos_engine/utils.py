"""Utility helpers for the chaos engine."""

from __future__ import annotations

from datetime import datetime, timezone


def utcnow() -> str:
    """Return an ISO 8601 timestamp in UTC."""
    return datetime.now(timezone.utc).isoformat()
