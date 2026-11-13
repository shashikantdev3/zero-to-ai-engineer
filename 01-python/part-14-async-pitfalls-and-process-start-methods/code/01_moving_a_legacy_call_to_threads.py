"""Zero to AI Engineer · Python · Part 14 of 25
Slide: Moving a legacy call to threads
Run: python 01_moving_a_legacy_call_to_threads.py
"""
import asyncio, time

def legacy_call(x: int) -> int:
    time.sleep(0.2)  # blocking
    return x * 2

async def main():
    # wrong here: legacy_call(1)
    jobs = [asyncio.to_thread(legacy_call, i)
            for i in range(5)]
    print(await asyncio.gather(*jobs))
asyncio.run(main(), debug=True)
