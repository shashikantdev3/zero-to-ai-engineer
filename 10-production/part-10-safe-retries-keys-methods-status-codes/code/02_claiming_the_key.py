"""Zero to AI Engineer · Production and LLMOps · Part 10 of 38
Slide: Claiming the key
Run: python 02_claiming_the_key.py
"""
async def create_ticket(key, payload):
    rkey = f"idem:{key}"
    ph = payload_hash(payload)
    state = {"state": "pending", "ph": ph}
    claimed = await redis.set(
        rkey, json.dumps(state),
        nx=True, ex=PENDING_TTL)
    if not claimed:
        return await check_repeat(rkey, ph)
    return await run_once(rkey, ph, payload)
