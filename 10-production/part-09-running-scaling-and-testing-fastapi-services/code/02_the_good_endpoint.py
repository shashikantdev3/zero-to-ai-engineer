"""Zero to AI Engineer · Production and LLMOps · Part 9 of 38
Slide: The good endpoint
Run: python 02_the_good_endpoint.py
"""
# Needs: pip install fastapi httpx
# (not run while building this repo, because the package was not installed there)
import httpx
from fastapi import Depends

async def http_client():
    async with httpx.AsyncClient() as c:
        yield c

@app.get("/good")
async def good(client=Depends(http_client)):
    return (await client.get(URL)).json()
