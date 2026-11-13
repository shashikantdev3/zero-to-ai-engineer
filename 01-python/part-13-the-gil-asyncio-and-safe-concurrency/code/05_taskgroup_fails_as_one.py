"""Zero to AI Engineer · Python · Part 13 of 25
Slide: TaskGroup fails as one
Run: python 05_taskgroup_fails_as_one.py
"""
import asyncio
async def work(i):
    if i == 2: raise ValueError(i)
    return i
async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            for i in range(4):
                tg.create_task(work(i))
    except* ValueError as eg:
        print("group failed:", eg.exceptions)
asyncio.run(main())
