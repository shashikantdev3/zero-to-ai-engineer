"""Zero to AI Engineer · Production and LLMOps · Part 10 of 38
Slide: Handling a repeated key
Run: python 03_handling_a_repeated_key.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
from fastapi import HTTPException

async def check_repeat(rkey, ph):
    raw = await redis.get(rkey)
    if raw is None:
        raise HTTPException(409, "Retry")
    stored = json.loads(raw)
    if stored["ph"] != ph:
        raise HTTPException(422, "Key reused")
    if stored["state"] == "pending":
        raise HTTPException(409, "Pending")
    return stored["result"]
