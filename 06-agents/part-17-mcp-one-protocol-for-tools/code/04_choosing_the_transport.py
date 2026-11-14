"""Zero to AI Engineer · Agents and Tools · Part 17 of 26
Slide: Choosing the transport
Run: python 04_choosing_the_transport.py
"""
# Needs: pip install mcp
# (not run while building this repo, because the package was not installed there)
import logging
import sys
from mcp.server.fastmcp import FastMCP
# stdout is the protocol stream
logging.basicConfig(
    stream=sys.stderr, level=logging.INFO)
mcp = FastMCP("ops")
if "--remote" in sys.argv:
    # remote: put auth and TLS in front
    mcp.run(transport="streamable-http")
else:
    mcp.run()  # stdio, the default
