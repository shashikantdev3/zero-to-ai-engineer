"""Zero to AI Engineer · Agents and Tools · Part 17 of 26
Slide: A prompt template
Run: python 02_a_prompt_template.py
"""
# Needs: pip install mcp
# (not run while building this repo, because the package was not installed there)
# --- repeated from 01_a_resource_in_python.py so this file runs on its own ---
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ops")

def load_runbook(name: str) -> str:
    return f"{name}: restart, then verify."

@mcp.resource("runbook://{name}")
def runbook(name: str) -> str:
    """A runbook as plain text."""
    return load_runbook(name)

# --- this slide ---
@mcp.prompt()
def triage(incident_id: str) -> str:
    return (
        f"Triage incident {incident_id}. "
        "Quote evidence for every claim."
    )
