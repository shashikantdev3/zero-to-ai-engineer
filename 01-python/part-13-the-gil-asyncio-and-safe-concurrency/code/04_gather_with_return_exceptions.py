"""Zero to AI Engineer · Python · Part 13 of 25
Slide: gather with return_exceptions
Run: python 04_gather_with_return_exceptions.py
"""
import asyncio
async def work(i):
    await asyncio.sleep(0.01)
    if i == 2:
        raise ValueError(i)
    return i
async def main():
    jobs = (work(i) for i in range(4))
    res = await asyncio.gather(
        *jobs, return_exceptions=True)
    print(res)
asyncio.run(main())
