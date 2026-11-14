"""Zero to AI Engineer · Production and LLMOps · Part 4 of 38
Slide: The POST route that streams
Run: python 02_the_post_route_that_streams.py
"""
# Needs: pip install fastapi pydantic
# (not run while building this repo, because the package was not installed there)
from fastapi import FastAPI, responses
from pydantic import BaseModel
app = FastAPI()
class ChatIn(BaseModel):
    message: str
@app.post("/v1/chat/stream")
def chat_stream(body: ChatIn):
    m = [{"role": "user",
          "content": body.message}]
    return responses.StreamingResponse(sse(m),
        media_type="text/event-stream",
        headers={"X-Accel-Buffering": "no"})
