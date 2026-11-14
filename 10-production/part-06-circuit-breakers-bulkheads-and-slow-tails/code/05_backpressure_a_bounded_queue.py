"""Zero to AI Engineer · Production and LLMOps · Part 6 of 38
Slide: Backpressure: a bounded queue
Run: python 05_backpressure_a_bounded_queue.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
from fastapi import HTTPException

work_q = asyncio.Queue(maxsize=1_000)

def admit(item):
    try:
        work_q.put_nowait(item)
    except asyncio.QueueFull:
        raise HTTPException(
            503, headers={"Retry-After": "5"})
