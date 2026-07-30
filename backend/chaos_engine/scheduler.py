"""Simple scheduler primitives for running periodic actions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, List, Optional


@dataclass
class ScheduledTask:
    name: str
    action: Callable[[], None]
    interval_seconds: int
    next_run: Optional[float] = None


class Scheduler:
    """A minimal scheduler that stores and executes tasks."""

    def __init__(self) -> None:
        self._tasks: List[ScheduledTask] = []

    def add_task(self, name: str, action: Callable[[], None], interval_seconds: int = 1) -> None:
        self._tasks.append(ScheduledTask(
            name=name, action=action, interval_seconds=interval_seconds))

    def run(self, iterations: int = 1) -> None:
        for _ in range(iterations):
            for task in self._tasks:
                task.action()
