"""Zero to AI Engineer · Agents and Tools · Part 17 of 26
Slide: A resource in Python
Run: python 01_a_resource_in_python.py
"""
# Needs: pip install mcp
# (not run while building this repo, because the package was not installed there)
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ops")

def load_runbook(name: str) -> str:
    return f"{name}: restart, then verify."

@mcp.resource("runbook://{name}")
def runbook(name: str) -> str:
    """A runbook as plain text."""
    return load_runbook(name)
