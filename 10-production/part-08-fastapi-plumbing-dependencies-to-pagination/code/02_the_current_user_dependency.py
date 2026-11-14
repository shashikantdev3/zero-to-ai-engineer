"""Zero to AI Engineer · Production and LLMOps · Part 8 of 38
Slide: The current user dependency
Run: python 02_the_current_user_dependency.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
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
