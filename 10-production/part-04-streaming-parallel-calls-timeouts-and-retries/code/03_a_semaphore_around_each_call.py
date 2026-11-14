"""Zero to AI Engineer · Production and LLMOps · Part 4 of 38
Slide: A semaphore around each call
Run: python 03_a_semaphore_around_each_call.py
"""
import asyncio
sem = asyncio.Semaphore(20)
async def bounded(coro):
    async with sem:
        return await coro
# stand-in for a search or a lookup
async def fake(name, secs):
    await asyncio.sleep(secs)
    return name
