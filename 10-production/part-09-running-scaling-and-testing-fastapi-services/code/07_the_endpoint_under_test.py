"""Zero to AI Engineer · Production and LLMOps · Part 9 of 38
Slide: The endpoint under test
Run: python 07_the_endpoint_under_test.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
# --- repeated from 06_app_setup_and_a_fake_model.py so this file runs on its own ---
import json
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
app = FastAPI()
PROBLEM = "application/problem+json"
def current_user(): return None
def llm_client(): return None
class FakeLLM:
    def __init__(self, reply):
        self.reply = reply
    async def complete(self, prompt):
        return self.reply

# --- this slide ---
@app.post("/v1/ask")
async def ask(body: dict,
              user=Depends(current_user),
              llm=Depends(llm_client)):
    raw = await llm.complete(body["question"])
    try:
        return json.loads(raw)
    except ValueError:
        err = {"retryable": True}
        return JSONResponse(err, 502,
            media_type=PROBLEM)
