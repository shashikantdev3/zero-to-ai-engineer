"""Zero to AI Engineer · Python · Part 13 of 25
Follow-along lab: Watch the loop take turns
Run: python 03_lab_watch_the_loop_take_turns.py
"""
import asyncio
async def step(name, delay):
    print(name, "starts")
    await asyncio.sleep(delay)
    print(name, "done")
async def main():
    coro = step("X", 0)
    print(type(coro).__name__)
    coro.close()
    a = asyncio.create_task(step("A", 0.02))
    b = asyncio.create_task(step("B", 0.01))
    await asyncio.wait([a, b])
asyncio.run(main())
