"""Zero to AI Engineer · Python · Part 15 of 25
Follow-along lab: Watch a Deadline Split a Batch
Run: python 04_lab_watch_a_deadline_split_a_batch.py
"""
import asyncio
async def main():
    ts = [asyncio.create_task(
        asyncio.sleep(s, result=s))
        for s in (0.1, 0.2, 2)]
    d, p = await asyncio.wait(ts, timeout=0.5)
    for t in p: t.cancel()
    await asyncio.gather(
        *p, return_exceptions=True)
    r = sorted(t.result() for t in d)
    print("done:", r)
    print("timed out:", len(p))
    print("cancelled:", p.pop().cancelled())
asyncio.run(main())
