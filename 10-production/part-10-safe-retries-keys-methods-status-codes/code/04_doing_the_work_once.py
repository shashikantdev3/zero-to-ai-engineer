"""Zero to AI Engineer · Production and LLMOps · Part 10 of 38
Slide: Doing the work once
Run: python 04_doing_the_work_once.py
"""
async def run_once(rkey, ph, payload):
    try:
        result = await tickets.create(payload)
    except Exception:
        # free the key so a retry can run
        await redis.delete(rkey)
        raise
    done = {"state": "done", "ph": ph,
            "result": result}
    await redis.set(rkey, json.dumps(done),
                    ex=DONE_TTL)
    return result
