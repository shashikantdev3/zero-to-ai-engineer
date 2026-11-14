"""Zero to AI Engineer · Agents and Tools · Part 18 of 26
Slide: A read-only tool with FastMCP
Run: python 04_a_read_only_tool_with_fastmcp.py
"""
# Needs: pip install mcp
# (not run while building this repo, because the package was not installed there)
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
