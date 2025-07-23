"""tools.code_exec – limited shell / python execution."""
import subprocess, sys, textwrap, tempfile, json, shlex

def run_bash(command: str, timeout: int = 10) -> str:
    """Run *command* in /bin/bash, return stdout/stderr."""
    try:
        completed = subprocess.run(command, shell=True, capture_output=True,
                                   text=True, timeout=timeout)
        return json.dumps({
            "stdout": completed.stdout,
            "stderr": completed.stderr,
            "exit_code": completed.returncode
        })
    except subprocess.TimeoutExpired:
        return json.dumps({"error": "timeout"})
