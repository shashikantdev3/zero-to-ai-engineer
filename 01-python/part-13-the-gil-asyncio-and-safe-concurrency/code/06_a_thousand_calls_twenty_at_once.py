"""Zero to AI Engineer · Python · Part 13 of 25
Slide: A thousand calls, twenty at once
Run: python 06_a_thousand_calls_twenty_at_once.py
"""
import asyncio
async def call_llm(prompt: str) -> str:
    await asyncio.sleep(0.05)
    return prompt.upper()
async def run_all(ps, limit=20):
    sem = asyncio.Semaphore(limit)
    async def one(p):
        async with sem:
            return await call_llm(p)
    return await asyncio.gather(*map(one, ps))
qs = [f"q{i}" for i in range(1000)]
print(len(asyncio.run(run_all(qs))))
