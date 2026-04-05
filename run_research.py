"""
AutoResearch Loop Runner
========================
Runs Claude Code in a loop, each iteration reads task.md and performs
one evolve-research cycle. Progress is tracked in progress.md.

Usage:
    python run_research.py

Configure:
    - Edit task.md with your project-specific instructions
    - Set PROJECT_DIR below to your project's working directory
"""

import subprocess
import sys
import json
import os

# ── Configuration ──────────────────────────────────────────────
# Set this to the absolute path of your project directory.
# Claude will run with this as its working directory.
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# The prompt sent to Claude each loop iteration.
PROMPT = "Read task.md and perform the evolve research loop"
# ───────────────────────────────────────────────────────────────


def stream_claude(prompt, cwd):
    """Run claude and stream its output in real-time."""
    cmd = [
        "claude", "-p", prompt,
        "--dangerously-skip-permissions",
        "--output-format", "stream-json",
        "--verbose",
    ]

    process = subprocess.Popen(
        cmd,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.DEVNULL,
    )

    for line in process.stdout:
        line = line.decode("utf-8", errors="replace").strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            print(line, flush=True)
            continue

        t = event.get("type", "")

        # Assistant text messages
        if t == "assistant":
            msg = event.get("message", {})
            for block in msg.get("content", []):
                if block.get("type") == "text":
                    print(block["text"], flush=True)
                elif block.get("type") == "tool_use":
                    name = block.get("name", "")
                    inp = block.get("input", {})
                    if name == "Bash":
                        print(f"\n> [TOOL] Bash: {inp.get('command', '')}", flush=True)
                    elif name == "Read":
                        print(f"\n> [TOOL] Read: {inp.get('file_path', '')}", flush=True)
                    elif name == "Edit":
                        print(f"\n> [TOOL] Edit: {inp.get('file_path', '')}", flush=True)
                    elif name == "Write":
                        print(f"\n> [TOOL] Write: {inp.get('file_path', '')}", flush=True)
                    elif name == "Glob":
                        print(f"\n> [TOOL] Glob: {inp.get('pattern', '')}", flush=True)
                    elif name == "Grep":
                        print(f"\n> [TOOL] Grep: {inp.get('pattern', '')}", flush=True)
                    else:
                        print(f"\n> [TOOL] {name}", flush=True)

        # Final result
        elif t == "result":
            cost = event.get("total_cost_usd", 0)
            turns = event.get("num_turns", 0)
            duration = event.get("duration_ms", 0)
            print(f"\n--- Done | {turns} turns | {duration/1000:.1f}s | ${cost:.4f} ---", flush=True)

    process.wait()
    return process.returncode


def main():
    print(f"Project directory: {PROJECT_DIR}")
    print(f"Prompt: {PROMPT}\n")

    loops = int(input("How many research loops to run? "))

    total_cost = 0.0

    for i in range(1, loops + 1):
        print(f"\n{'='*60}", flush=True)
        print(f"  Research Loop {i} of {loops}", flush=True)
        print(f"{'='*60}\n", flush=True)

        returncode = stream_claude(PROMPT, PROJECT_DIR)

        if returncode != 0:
            print(f"\nLoop {i} exited with code {returncode}", flush=True)

    print(f"\n{'='*60}", flush=True)
    print(f"  All {loops} research loops complete.", flush=True)
    print(f"{'='*60}", flush=True)


if __name__ == "__main__":
    main()
