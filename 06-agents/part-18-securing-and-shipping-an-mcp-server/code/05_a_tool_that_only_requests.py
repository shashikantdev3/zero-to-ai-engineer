"""Zero to AI Engineer · Agents and Tools · Part 18 of 26
Slide: A tool that only requests
Run: python 05_a_tool_that_only_requests.py
"""
# Needs: pip install mcp
# (not run while building this repo, because the package was not installed there)
# --- repeated from 04_a_read_only_tool_with_fastmcp.py so this file runs on its own ---
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ops-look")

@mcp.tool()
def service_status(service: str) -> dict:
    """Read-only. Return current health and
    last deploy time for ONE service. Use
    before proposing any change. Never
    changes anything."""
    # real version: read-only credential
    return {"service": service, "ok": True}

# --- this slide ---
@mcp.tool()
def request_change(incident_id: str,
                   plan_id: str,
                   summary: str) -> dict:
    """Create a change REQUEST for human
    approval. Does not execute anything."""
    # real version: add to a change queue
    return {"incident": incident_id,
            "plan": plan_id, "queued": True}

if __name__ == "__main__":
    mcp.run()
