"""Zero to AI Engineer · Production and LLMOps · Part 8 of 38
Slide: Using the dependencies
Run: python 03_using_the_dependencies.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
# --- repeated from 02_the_current_user_dependency.py so this file runs on its own ---
from fastapi import HTTPException, Request
from fastapi.security import (
    HTTPAuthorizationCredentials as Creds)

async def current_user(
        creds: Creds = Depends(bearer)):
    try:
        return verify(creds.credentials)
    except jwt.PyJWTError:
        raise HTTPException(401, headers={
            "WWW-Authenticate": "Bearer"})

# --- this slide ---
def llm_client(request: Request):
    # created once in the lifespan
    return request.app.state.llm

@app.get("/v1/me")
async def me(user=Depends(current_user)):
    return {"sub": user["sub"]}
