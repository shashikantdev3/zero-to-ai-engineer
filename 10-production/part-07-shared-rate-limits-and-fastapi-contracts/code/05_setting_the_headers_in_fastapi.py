"""Zero to AI Engineer · Production and LLMOps · Part 7 of 38
Slide: Setting the headers in FastAPI
Run: python 05_setting_the_headers_in_fastapi.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
from fastapi import HTTPException, Response
def rate_headers(resp: Response, limit: int,
                 left: int, reset_s: int):
    h = resp.headers
    rem = max(0, left)
    h["X-RateLimit-Limit"] = str(limit)
    h["X-RateLimit-Remaining"] = str(rem)
    h["X-RateLimit-Reset"] = str(reset_s)
def throttled(retry_after_s: int):
    hdr = {"Retry-After": str(retry_after_s)}
    raise HTTPException(
        429, "Too many requests", headers=hdr)
