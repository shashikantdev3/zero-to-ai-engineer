"""Zero to AI Engineer · Agents and Tools · Part 15 of 26
Slide: Check the release pages yourself
Run: python 02_check_the_release_pages_yourself.py
"""
# Check release state on the day.
# pip index is experimental in pip.
import subprocess
import sys

pkgs = ["semantic-kernel",
        "autogen-agentchat",
        "agent-framework"]
for name in pkgs:
    cmd = [sys.executable, "-m", "pip",
           "index", "versions", name]
    subprocess.run(cmd)
