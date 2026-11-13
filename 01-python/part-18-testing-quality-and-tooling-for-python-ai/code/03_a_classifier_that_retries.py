"""Zero to AI Engineer · Python · Part 18 of 25
Slide: A classifier that retries
Run: python 03_a_classifier_that_retries.py
"""
import asyncio
class RateLimited(Exception): ...
async def classify(client, text, attempts=3):
    for i in range(attempts):
        try:
            r = await client.complete(
                prompt=f"Classify: {text}")
            return r.strip().lower()
        except RateLimited:
            if i == attempts - 1:
                raise
            await asyncio.sleep(0)
