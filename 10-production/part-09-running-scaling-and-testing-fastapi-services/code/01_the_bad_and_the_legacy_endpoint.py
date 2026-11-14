"""Zero to AI Engineer · Production and LLMOps · Part 9 of 38
Slide: The bad and the legacy endpoint
Run: python 01_the_bad_and_the_legacy_endpoint.py
"""
# Needs: pip install fastapi requests
# (not run while building this repo, because the package was not installed there)
import asyncio, time
import requests
from fastapi import FastAPI
app = FastAPI()
URL = "https://example.com/data"
def slow_sdk(): time.sleep(1); return {}
@app.get("/bad")
async def bad():
    return requests.get(URL).json()
@app.get("/legacy")
async def legacy():
    return await asyncio.to_thread(slow_sdk)
