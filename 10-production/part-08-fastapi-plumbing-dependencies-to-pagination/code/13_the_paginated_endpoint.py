"""Zero to AI Engineer · Production and LLMOps · Part 8 of 38
Slide: The paginated endpoint
Run: python 13_the_paginated_endpoint.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
# --- repeated from 12_router_and_data_stand_ins.py so this file runs on its own ---
from fastapi import APIRouter, FastAPI

app = FastAPI()
v1 = APIRouter(prefix="/v1")

# stand-ins for your data layer
class FakeDB:
    async def page(self, after, limit):
        return []
db = FakeDB()
encode = str
decode = lambda c: c

# --- this slide ---
@v1.get("/conversations")
async def list_conv(limit: int = 50,
        cursor: str | None = None):
    rows = await db.page(
        after=decode(cursor), limit=limit + 1)
    nxt = None
    if len(rows) > limit:
        nxt = encode(rows[limit - 1].sort_key)
    return {"items": rows[:limit],
            "next_cursor": nxt}

app.include_router(v1)
