"""Zero to AI Engineer · Python · Part 15 of 25
Slide: The Client in Async With
Run: python 06_the_client_in_async_with.py
"""
# Needs: pip install httpx
from contextlib import asynccontextmanager
import httpx

@asynccontextmanager
async def llm_client():
    client = httpx.AsyncClient(timeout=30)
    try:
        yield client
    finally:
        await client.aclose()
