"""Zero to AI Engineer · Agents and Tools · Part 15 of 26
Slide: An audit middleware, simulated
Run: python 01_an_audit_middleware_simulated.py
"""
import asyncio

async def audit(ctx, call_next):
    print("before:", ctx["function"])
    await call_next(ctx)
    ctx["result"] = "[redacted]"
    print("after:", ctx["result"])

async def tool_call(ctx):
    ctx["result"] = "card 4242"
ctx = {"function": "lookup"}
asyncio.run(audit(ctx, tool_call))
