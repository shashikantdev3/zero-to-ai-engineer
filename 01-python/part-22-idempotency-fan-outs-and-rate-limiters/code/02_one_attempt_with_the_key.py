"""Zero to AI Engineer · Python · Part 22 of 25
Slide: One attempt, with the key
Run: python 02_one_attempt_with_the_key.py
"""
# Needs: pip install httpx
import httpx
async def attempt(client, payload, key):
    try:
        r = await client.post(
            "/tickets", json=payload,
            headers={"Idempotency-Key": key})
    except httpx.TransportError as e:
        raise RetryableError(repr(e)) from e
    if r.status_code in RETRYABLE_STATUS:
        raise RetryableError(r.status_code)
    r.raise_for_status()
    return r.json()
