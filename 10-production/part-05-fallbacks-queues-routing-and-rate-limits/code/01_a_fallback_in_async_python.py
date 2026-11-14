"""Zero to AI Engineer · Production and LLMOps · Part 5 of 38
Slide: A Fallback in Async Python
Run: python 01_a_fallback_in_async_python.py
"""
import asyncio
class Throttled(Exception): pass
class UpstreamDown(Exception): pass
async def primary(req): raise Throttled()
async def fallback(req): return "ok: " + req
async def generate(req):
    try:
        return await primary(req), "primary"
    except (Throttled, UpstreamDown,
            asyncio.TimeoutError):
        return await fallback(req), "fallback"
print(asyncio.run(generate("hi")))
