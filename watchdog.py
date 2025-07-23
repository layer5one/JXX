"""watchdog.py
Monitors orchestrator.py, restarts on crash, and stores crash log to MemOS.
"""
import subprocess, sys, os, uuid, shlex, time, signal
from memory.memory_manager import MemoryManager

mm = MemoryManager()

def run():
    session_id = str(uuid.uuid4())
    while True:
        print(f"🚀 Launching orchestrator (session {session_id})")
        cmd = [sys.executable, "orchestrator.py", "--session-id", session_id]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        # Stream output
        for line in proc.stdout:
            print(line, end="")

        proc.wait()
        if proc.returncode == 0:
            print("🎉 Orchestrator exited cleanly.")
            break
        else:
            print("⚠️  Orchestrator crashed – restarting with --recovering.")
            crash_log = f"Return code: {proc.returncode}"
            mm.append_crash_log(session_id, crash_log)
            time.sleep(1)  # back‑off
            cmd = [sys.executable, "orchestrator.py", "--session-id", session_id, "--recovering"]
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("🛑 Watchdog terminated by user.")
