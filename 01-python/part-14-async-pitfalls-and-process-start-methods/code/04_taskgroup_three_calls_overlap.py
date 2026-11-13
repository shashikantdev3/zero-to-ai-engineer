"""Zero to AI Engineer · Python · Part 14 of 25
Slide: TaskGroup: three calls overlap
Run: python 04_taskgroup_three_calls_overlap.py
"""
import asyncio, time
async def work(i: int) -> int:
    await asyncio.sleep(1)
    return i
async def main():
    t1 = time.perf_counter()
    async with asyncio.TaskGroup() as tg:
        ts = [tg.create_task(work(i))
              for i in range(3)]
    print(round(time.perf_counter() - t1),
          [t.result() for t in ts])
asyncio.run(main())
