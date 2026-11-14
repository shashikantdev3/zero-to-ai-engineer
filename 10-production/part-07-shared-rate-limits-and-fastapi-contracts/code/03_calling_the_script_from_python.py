"""Zero to AI Engineer · Production and LLMOps · Part 7 of 38
Slide: Calling the script from Python
Run: python 03_calling_the_script_from_python.py
"""
# Needs: pip install redis
# (not run while building this repo, because the package was not installed there)
import redis.asyncio as redis
r = redis.from_url("redis://localhost:6379")
# handles EVALSHA and reload for you
take = r.register_script(LUA)

async def allow(tenant: str, n: int) -> bool:
    res = await take(
        keys=[f"rl:{tenant}"],
        args=[60_000, 1_000, n],
    )
    return res == 1
