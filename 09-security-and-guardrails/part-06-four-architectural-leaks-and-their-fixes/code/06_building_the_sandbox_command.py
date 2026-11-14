"""Zero to AI Engineer · Security and Guardrails · Part 6 of 11
Slide: Building the sandbox command
Run: python 06_building_the_sandbox_command.py
"""
# Build the sandbox command as a list.
cmd = ["docker", "run", "--rm"]
# no network, throwaway filesystem
cmd += ["--network", "none"]
cmd += ["--read-only", "--tmpfs", "/tmp"]
# non-root user, no extra powers
cmd += ["--user", "65534:65534"]
cmd += ["--cap-drop", "ALL"]
cmd += ["--security-opt", "no-new-privileges"]
