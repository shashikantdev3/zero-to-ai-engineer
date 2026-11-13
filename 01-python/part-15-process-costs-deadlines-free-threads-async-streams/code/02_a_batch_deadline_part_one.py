"""Zero to AI Engineer · Python · Part 15 of 25
Slide: A Batch Deadline, Part One
Run: python 02_a_batch_deadline_part_one.py
"""
import asyncio
async def batch(coros, deadline: float):
    tasks = {asyncio.create_task(c): i
             for i, c in enumerate(coros)}
    done, pending = await asyncio.wait(
        tasks, timeout=deadline)
    for t in pending:
        t.cancel()
    # let cancellations finish
    await asyncio.gather(
        *pending, return_exceptions=True)
    return split(tasks, done, pending)
