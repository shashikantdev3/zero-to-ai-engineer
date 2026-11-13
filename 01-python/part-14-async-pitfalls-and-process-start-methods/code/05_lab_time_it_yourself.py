"""Zero to AI Engineer · Python · Part 14 of 25
Follow-along lab: Time it yourself
Run: python 05_lab_time_it_yourself.py
"""
import asyncio, time
now = time.perf_counter
async def work():
    await asyncio.sleep(0.1)
async def main():
    t = asyncio.create_task(work())
    print("is future:", asyncio.isfuture(t))
    s = now()
    for _ in range(3): await work()
    print("in order:", round(now() - s, 1))
    s = now()
    await asyncio.gather(t, work(), work())
    print("together:", round(now() - s, 1))
asyncio.run(main())
