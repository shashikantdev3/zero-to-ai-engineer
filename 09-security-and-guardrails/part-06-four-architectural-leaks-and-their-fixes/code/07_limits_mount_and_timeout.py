"""Zero to AI Engineer · Security and Guardrails · Part 6 of 11
Slide: Limits, mount, and timeout
Run: python 07_limits_mount_and_timeout.py
"""
# --- repeated from 06_building_the_sandbox_command.py so this file runs on its own ---
# Build the sandbox command as a list.
cmd = ["docker", "run", "--rm"]
# no network, throwaway filesystem
cmd += ["--network", "none"]
cmd += ["--read-only", "--tmpfs", "/tmp"]
# non-root user, no extra powers
cmd += ["--user", "65534:65534"]
cmd += ["--cap-drop", "ALL"]
cmd += ["--security-opt", "no-new-privileges"]

# --- this slide ---
# memory, CPU and process limits
cmd += ["--memory", "512m", "--cpus", "1"]
cmd += ["--pids-limit", "64"]
# mount only the job file, read-only
cmd += ["-v", "$PWD/job.py:/job/job.py:ro"]
cmd += ["python:3.12-slim"]
# stop the job after ten seconds
cmd += ["timeout", "10"]
cmd += ["python", "/job/job.py"]
print(" ".join(cmd))
