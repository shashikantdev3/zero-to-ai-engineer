"""Zero to AI Engineer · Production and LLMOps · Part 3 of 38
Slide: Honour the header, add jitter
Run: python 03_honour_the_header_add_jitter.py
"""
# --- repeated from 02_reading_every_retry_after_form.py so this file runs on its own ---
def retry_after_seconds(h, default=1.0):
    # provider-specific header, check first
    if "retry-after-ms" in h:
        ms = float(h["retry-after-ms"])
        return ms / 1000
    value = h.get("retry-after")
    if value is None:
        return default
    try:
        return float(value)
    except ValueError:
        return seconds_until(value, default)

# --- this slide ---
import asyncio, random

headers = {"retry-after": "2"}
status_code = 429

async def main():
    if status_code == 429:
        wait = retry_after_seconds(headers)
        wait += random.uniform(0, 0.5)
        await asyncio.sleep(wait)

asyncio.run(main())
