"""Zero to AI Engineer · Production and LLMOps · Part 9 of 38
Slide: A stand-in model stream
Run: python 04_a_stand_in_model_stream.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
from fastapi import FastAPI, WebSocket
from fastapi import WebSocketDisconnect
app = FastAPI()

async def llm_stream(text):
    for word in text.split():
        yield word + " "
