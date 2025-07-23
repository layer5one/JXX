"""tools.file_system – simple file utilities exposed as LLM tools."""
from pathlib import Path

def read_file(path: str) -> str:
    """Return the file's contents or error message."""
    try:
        return Path(path).read_text()
    except Exception as e:
        return f"Error reading {path}: {e}"

def write_file(path: str, content: str) -> str:
    """Overwrite *path* with *content* and return confirmation."""
    try:
        Path(path).write_text(content)
        return f"Wrote {len(content)} bytes to {path}"
    except Exception as e:
        return f"Error writing {path}: {e}"
