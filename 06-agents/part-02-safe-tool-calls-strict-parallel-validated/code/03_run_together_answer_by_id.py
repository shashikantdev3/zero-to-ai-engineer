"""Zero to AI Engineer · Agents and Tools · Part 2 of 26
Slide: Run together, answer by ID
Run: python 03_run_together_answer_by_id.py
"""
# --- repeated from 02_three_calls_with_their_own_ids.py so this file runs on its own ---
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

# --- this slide ---
async def one(c):
    try:
        fn = TOOLS[c.name]
        res = json.dumps(await fn(**c.input))
    except Exception:
        res = FAIL
    return {"type": "tool_result",
            "tool_use_id": c.id,
            "content": res}
async def run_calls(cs):
    return await asyncio.gather(*map(one, cs))
print(asyncio.run(run_calls(calls)))
