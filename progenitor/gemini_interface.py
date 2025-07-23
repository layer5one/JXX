"""progenitor.gemini_interface – thin wrapper for Google Gemini CLI."""
import subprocess, textwrap, shutil, os, tempfile

GEMINI_BIN = shutil.which("gemini") or "gemini"

def call_gemini(prompt:str) -> str:
    """Send *prompt* to Gemini CLI, return output (blocking)."""
    proc = subprocess.Popen([GEMINI_BIN], stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True)
    out, err = proc.communicate(prompt)
    if err:
        return f"Gemini error: {err}"
    return out
