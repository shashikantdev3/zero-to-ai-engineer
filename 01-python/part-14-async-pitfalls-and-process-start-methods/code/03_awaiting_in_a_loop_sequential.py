"""Zero to AI Engineer · Python · Part 14 of 25
Slide: Awaiting in a loop: sequential
Run: python 03_awaiting_in_a_loop_sequential.py
"""
import asyncio, time

async def work(i: int) -> int:
    await asyncio.sleep(1)
    return i

async def main():
    t0 = time.perf_counter()
    for i in range(3):
        await work(i)  # sequential
    print(round(time.perf_counter() - t0))
asyncio.run(main())
