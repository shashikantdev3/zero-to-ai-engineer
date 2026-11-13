"""Zero to AI Engineer · Python · Part 22 of 25
Slide: Fan out with limits
Run: python 04_fan_out_with_limits.py
"""
import asyncio

async def fan_out(items, call, *,
                  limit=10, secs=30.0):
    sem = asyncio.Semaphore(limit)
    async def one(item):
        async with sem:
            async with asyncio.timeout(secs):
                return await call(item)
    jobs = (one(i) for i in items)
    return await asyncio.gather(
        *jobs, return_exceptions=True)
