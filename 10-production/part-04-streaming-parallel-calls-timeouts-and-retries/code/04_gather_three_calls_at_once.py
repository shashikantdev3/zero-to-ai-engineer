"""Zero to AI Engineer · Production and LLMOps · Part 4 of 38
Slide: Gather three calls at once
Run: python 04_gather_three_calls_at_once.py
"""
# --- repeated from 03_a_semaphore_around_each_call.py so this file runs on its own ---
import asyncio
sem = asyncio.Semaphore(20)
async def bounded(coro):
    async with sem:
        return await coro
# stand-in for a search or a lookup
async def fake(name, secs):
    await asyncio.sleep(secs)
    return name

# --- this slide ---
async def main():
    return await asyncio.gather(
        bounded(fake("vector", 0.3)),
        bounded(fake("bm25", 0.2)),
        bounded(fake("acl", 0.1)),
        return_exceptions=True)
print(asyncio.run(main()))
