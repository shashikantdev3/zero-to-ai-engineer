"""Zero to AI Engineer · Python · Part 14 of 25
Slide: The missing await
Run: python 06_the_missing_await.py
"""
import asyncio

async def write_audit(event: str) -> None:
    await asyncio.sleep(0)
    print("audit", event)

async def handler():
    write_audit("refund")  # BUG: never runs
    await write_audit("refund")  # correct

asyncio.run(handler(), debug=True)
# notebook: await handler(), not asyncio.run
