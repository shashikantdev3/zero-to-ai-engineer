"""Zero to AI Engineer · Production and LLMOps · Part 4 of 38
Slide: The retry loop with full jitter
Run: python 07_the_retry_loop_with_full_jitter.py
"""
async def with_retry(fn, attempts=5):
    for i in range(attempts):
        try:
            return await fn()
        except Retryable as e:
            if i == attempts - 1:
                raise
            top = min(CAP, BASE * 2 ** i)
            d = random.uniform(0, top)
            if e.retry_after:
                d = max(d, e.retry_after)
            await asyncio.sleep(d)
