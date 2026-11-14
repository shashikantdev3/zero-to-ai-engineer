"""Zero to AI Engineer · Evaluation · Part 4 of 11
Slide: Shadow mode: the handler
Run: python 06_shadow_mode_the_handler.py
"""
async def shadow(req):
    try:
        job = candidate(req)
        res = await asyncio.wait_for(job, 10)
        log_shadow(req, res, None)
    except Exception as exc:
        log_shadow(req, None, repr(exc))
async def handle(req):
    t = asyncio.create_task(shadow(req))
    _tasks.add(t)
    t.add_done_callback(_tasks.discard)
    return await current(req)
