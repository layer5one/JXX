"""orchestrator.py
Top‑level orchestrator for Jaraxxus AI.
This is a *minimal functional stub* that demonstrates:
  • Session management
  • Simple planning → execution → response cycle
  • Crash simulation & recovery flag
Full LangGraph integration should replace the inline loops.
"""
import argparse, uuid, json, sys, traceback
from pathlib import Path
from typing import List
from agent_state import AgentState
from tools import file_system
from agents.specialist_file import run_file_specialist
from memory.memory_manager import MemoryManager

mm = MemoryManager()

def decompose_task(task:str)->List[str]:
    # TODO: Replace with LLM-driven planning. For now naive single step.
    return [task]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--session-id", type=str, default=None)
    parser.add_argument("--recovering", action="store_true")
    args = parser.parse_args()

    session_id = args.session_id or str(uuid.uuid4())
    state = AgentState(session_id=session_id,
                       task=None,
                       recovery_attempts=1 if args.recovering else 0)

    if not args.recovering:
        # Fresh task
        state.task = input("Jaraxxus task › ").strip()

    # Store initial state
    mm.update_scratchpad(state)

    try:
        steps = decompose_task(state.task)
        for step in steps:
            state.plan = f"Read file content: {step}"
            state.specialist = "FileSpecialist"
            state.tool_output = run_file_specialist(state.plan)
            mm.update_scratchpad(state)

        print(f"✅ Jaraxxus completed: {state.tool_output}")
        mm.update_scratchpad(state)
        sys.exit(0)

    except Exception as e:
        state.error = traceback.format_exc()
        mm.update_scratchpad(state)
        print("""💥 Orchestrator crashed – details stored to MemOS scratchpad""")
        sys.exit(1)

if __name__ == "__main__":
    main()
