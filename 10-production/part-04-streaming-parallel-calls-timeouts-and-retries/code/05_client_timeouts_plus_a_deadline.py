"""Zero to AI Engineer · Production and LLMOps · Part 4 of 38
Slide: Client timeouts plus a deadline
Run: python 05_client_timeouts_plus_a_deadline.py
"""
import asyncio, httpx
# inner budget: smaller than the outer one
client = httpx.AsyncClient(
    timeout=httpx.Timeout(10.0, connect=3.0))
async def call_model(client, req):
    # your model call, using this client
    await asyncio.sleep(0.1)
    return "ok"
async def handle(req):
    # outer deadline, Python 3.11+
    async with asyncio.timeout(20):
        return await call_model(client, req)
