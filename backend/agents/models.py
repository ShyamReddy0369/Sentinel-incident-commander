"""
Shared models used by AI agents.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class AnalysisReport:
    """
    Represents the complete AI analysis
    for an incident.
    """

    incident_id: str
    service_name: str
    severity: str

    diagnosis: dict
    execution_plan: dict
    remediation: dict

    generated_at: datetime = field(default_factory=datetime.utcnow)
