"""Zero to AI Engineer · Production and LLMOps · Part 8 of 38
Slide: The lifespan function
Run: python 04_the_lifespan_function.py
"""
# Needs: pip install fastapi httpx
# (not run while building this repo, because the package was not installed there)
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
