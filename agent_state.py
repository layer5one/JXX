"""agent_state.py
Typed state container for Jaraxxus orchestrator cycles.
"""
from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List

@dataclass
class AgentState:
    session_id: str
    task: Optional[str] = None
    plan: Optional[str] = None
    specialist: Optional[str] = None
    tool_output: Optional[str] = None
    error: Optional[str] = None
    recovery_attempts: int = 0
    root_cause: Optional[str] = None
    progenitor_result: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
