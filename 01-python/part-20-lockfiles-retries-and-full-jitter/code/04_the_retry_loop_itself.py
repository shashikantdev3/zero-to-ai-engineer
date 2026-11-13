"""Zero to AI Engineer · Python · Part 20 of 25
Slide: The retry loop itself
Run: python 04_the_retry_loop_itself.py
"""
async def retry(fn, dl, attempts=5):
    if attempts < 1:
        raise ValueError("attempts < 1")
    for i in range(attempts):
        try:
            return await attempt(fn, dl)
        except RetryableError as e:
            if i == attempts - 1:
                raise
            d = next_delay(i, e, dl)
            await asyncio.sleep(d)
