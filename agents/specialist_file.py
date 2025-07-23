"""agents.specialist_file – very naive File I/O specialist stub.
Replace with Ollama persona + LLM tool calling for production.
"""
from tools import file_system

def run_file_specialist(plan: str) -> str:
    """Extremely simplified: if plan starts with 'Read', call read_file."""
    plan_lower = plan.lower()
    if plan_lower.startswith("read"):
        path = plan.split(":", 1)[-1].strip()
        return file_system.read_file(path)
    elif plan_lower.startswith("write"):
        # expects 'Write <path>: <content>'
        try:
            header, content = plan.split(":", 1)
            path = header.split()[1]
            return file_system.write_file(path, content.strip())
        except Exception as e:
            return f"Parse error: {e}"
    else:
        return "FileSpecialist: Unrecognized plan."
