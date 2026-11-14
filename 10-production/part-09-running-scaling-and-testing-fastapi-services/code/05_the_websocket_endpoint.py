"""Zero to AI Engineer · Production and LLMOps · Part 9 of 38
Slide: The WebSocket endpoint
Run: python 05_the_websocket_endpoint.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
# --- repeated from 04_a_stand_in_model_stream.py so this file runs on its own ---
from fastapi import FastAPI, WebSocket
from fastapi import WebSocketDisconnect
app = FastAPI()

async def llm_stream(text):
    for word in text.split():
        yield word + " "

# --- this slide ---
@app.websocket("/v1/ws")
async def ws(socket: WebSocket):
    await socket.accept()
    try:
        while True:
            msg = await socket.receive_json()
            text = msg["text"]
            async for d in llm_stream(text):
                out = {"delta": d}
                await socket.send_json(out)
    except WebSocketDisconnect:
        pass
