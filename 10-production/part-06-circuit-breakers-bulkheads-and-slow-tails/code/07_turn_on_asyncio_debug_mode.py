"""Zero to AI Engineer · Production and LLMOps · Part 6 of 38
Slide: Turn on asyncio debug mode
Run: python 07_turn_on_asyncio_debug_mode.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
import asyncio, logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
logging.basicConfig(level=logging.DEBUG)

@asynccontextmanager
async def lifespan(app: FastAPI):
    loop = asyncio.get_running_loop()
    loop.set_debug(True)
    loop.slow_callback_duration = 0.05
    yield
app = FastAPI(lifespan=lifespan)
