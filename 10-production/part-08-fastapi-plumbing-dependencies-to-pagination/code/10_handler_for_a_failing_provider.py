"""Zero to AI Engineer · Production and LLMOps · Part 8 of 38
Slide: Handler for a failing provider
Run: python 10_handler_for_a_failing_provider.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
# --- repeated from 08_two_custom_exceptions.py, 09_one_builder_for_every_error.py so this file runs on its own ---
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()
BASE = "https://errors.example.com/"

class UpstreamModelError(Exception): ...
# invalid or unparseable model output
class ModelOutputError(Exception): ...

def problem(request, status, type_, title,
            detail, retryable, headers=None):
    body = {
        "type": type_, "title": title,
        "status": status, "detail": detail,
        "correlation_id": request.state.cid,
        "retryable": retryable}
    return JSONResponse(
        body, status_code=status,
        headers=headers,
        media_type="application/problem+json")

# --- this slide ---
@app.exception_handler(UpstreamModelError)
async def upstream(request: Request, exc):
    return problem(request, 503,
        BASE + "model-unavailable",
        "Model unavailable",
        "Please retry shortly.", True,
        {"Retry-After": "5"})
