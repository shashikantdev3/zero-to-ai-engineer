"""Zero to AI Engineer · Python · Part 14 of 25
Slide: A timeout around a slow call
Run: python 02_a_timeout_around_a_slow_call.py
"""
import asyncio
async def slow():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        raise  # cleanup first, then re-raise
async def main():
    try:
        async with asyncio.timeout(0.5):
            await slow()
    except TimeoutError: print("timed out")
asyncio.run(main())
