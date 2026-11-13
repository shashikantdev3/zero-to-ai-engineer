"""Zero to AI Engineer · Python · Part 15 of 25
Slide: Stop Early, Clean Up Now
Run: python 08_stop_early_clean_up_now.py
"""
from contextlib import aclosing
async def first_n(url, n):
    out = []
    async with llm_client() as c:
        gen = stream_lines(c, url)
        async with aclosing(gen) as lines:
            async for line in lines:
                out.append(line)
                if len(out) == n:
                    # cleanup runs now
                    break
    return out
