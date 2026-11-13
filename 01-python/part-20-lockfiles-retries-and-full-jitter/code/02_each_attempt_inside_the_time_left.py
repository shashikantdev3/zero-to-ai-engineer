"""Zero to AI Engineer · Python · Part 20 of 25
Slide: Each attempt inside the time left
Run: python 02_each_attempt_inside_the_time_left.py
"""
import asyncio, random, time
class DeadlineExceeded(Exception): ...
async def attempt(fn, dl):
    t = dl - time.monotonic()
    if t <= 0: raise DeadlineExceeded
    try:
        async with asyncio.timeout(t) as cm:
            return await fn()
    except TimeoutError as e:
        if cm.expired():
            raise DeadlineExceeded from e
        raise
