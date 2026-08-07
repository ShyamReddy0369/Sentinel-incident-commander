"""
Base class for all Sentinel AI agents.
"""

from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Every AI agent in Sentinel inherits from this class.
    """

    def __init__(self, name: str):

        self.name = name

    @abstractmethod
    def run(self, context):
        """
        Execute the agent.
        """
        pass
