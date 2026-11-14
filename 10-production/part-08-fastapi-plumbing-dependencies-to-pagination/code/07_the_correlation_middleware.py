"""Zero to AI Engineer · Production and LLMOps · Part 8 of 38
Slide: The correlation middleware
Run: python 07_the_correlation_middleware.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
# --- repeated from 06_the_id_format_rule.py so this file runs on its own ---
import re
import uuid
from fastapi import FastAPI, Request

app = FastAPI()
HDR = "x-correlation-id"
CID_OK = re.compile(r"[A-Za-z0-9-]{8,64}")

# --- this slide ---
@app.middleware("http")
async def cid_mw(request: Request, call_next):
    raw = request.headers.get(HDR, "")
    ok = CID_OK.fullmatch(raw)
    cid = raw if ok else str(uuid.uuid4())
    request.state.cid = cid
    resp = await call_next(request)
    resp.headers[HDR] = cid
    return resp
