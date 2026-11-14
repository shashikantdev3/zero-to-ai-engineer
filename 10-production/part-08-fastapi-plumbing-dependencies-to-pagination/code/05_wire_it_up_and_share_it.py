"""Zero to AI Engineer · Production and LLMOps · Part 8 of 38
Slide: Wire it up and share it
Run: python 05_wire_it_up_and_share_it.py
"""
# Needs: pip install fastapi httpx
# (not run while building this repo, because the package was not installed there)
# --- repeated from 04_the_lifespan_function.py so this file runs on its own ---
from contextlib import asynccontextmanager
import httpx
from fastapi import FastAPI, Request

@asynccontextmanager
async def lifespan(app: FastAPI):
    t = httpx.Timeout(10.0, connect=3.0)
    client = httpx.AsyncClient(timeout=t)
    app.state.http = client
    yield
    await client.aclose()

# --- this slide ---
app = FastAPI(lifespan=lifespan)

def http_client(request: Request):
    return request.app.state.http
