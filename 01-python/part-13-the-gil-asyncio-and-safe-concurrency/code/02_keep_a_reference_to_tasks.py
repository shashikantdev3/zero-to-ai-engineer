"""Zero to AI Engineer · Python · Part 13 of 25
Slide: Keep a reference to tasks
Run: python 02_keep_a_reference_to_tasks.py
"""
import asyncio
background: set[asyncio.Task] = set()
async def fetch(i: int) -> int:
    # stands in for a network call
    await asyncio.sleep(0.1)
    return i
async def main():
    t = asyncio.create_task(fetch(99))
    background.add(t)
    t.add_done_callback(background.discard)
    return await fetch(1)
print(asyncio.run(main()))
