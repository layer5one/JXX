"""memory.memory_manager – wrapper around MemOS (gracefully degrades if MemOS absent)."""
import json, os, datetime, warnings
from typing import Any
from agent_state import AgentState

try:
    from memos.configs.mem_os import MOSConfig
    from memos.mem_os.main import MOS
    _MEMOS_AVAILABLE = True
except ImportError:
    warnings.warn("MemOS library not available – memory disabled.")
    _MEMOS_AVAILABLE = False

class MemoryManager:
    def __init__(self, config_path:str = "config/memos_config.json"):
        self.enabled = _MEMOS_AVAILABLE
        if self.enabled:
            self.client = MOS(MOSConfig.from_json_file(config_path))
        else:
            self.client = None

    def update_scratchpad(self, state: AgentState):
        if not self.enabled:
            return
        self.client.add(messages=[{
            "role": "system",
            "content": state.__dict__
        }], user_id=state.session_id)

    def append_crash_log(self, session_id:str, log:str):
        if not self.enabled:
            return
        self.client.add(messages=[{
            "role": "system",
            "content": {"session_id": session_id,
                        "crash_log": log,
                        "timestamp": datetime.datetime.utcnow().isoformat()}
        }], user_id=session_id)
