"""Zero to AI Engineer · Agents and Tools · Part 2 of 26
Slide: Three calls with their own IDs
Run: python 02_three_calls_with_their_own_ids.py
"""
import asyncio, json
from types import SimpleNamespace as NS
async def status(svc):
    await asyncio.sleep(0.01)
    return {"svc": svc, "up": True}

TOOLS = {"status": status}
FAIL = '{"ok": false, "error": "TOOL_FAILED"}'
names = ["db", "api", "web"]
calls = [NS(id=f"tu_{i}", name="status",
            input={"svc": n})
         for i, n in enumerate(names)]
