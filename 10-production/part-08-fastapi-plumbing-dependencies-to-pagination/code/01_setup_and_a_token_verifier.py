"""Zero to AI Engineer · Production and LLMOps · Part 8 of 38
Slide: Setup and a token verifier
Run: python 01_setup_and_a_token_verifier.py
"""
# Needs: pip install fastapi jwt
# (not run while building this repo, because the package was not installed there)
import os
import jwt
from fastapi import Depends, FastAPI
from fastapi.security import HTTPBearer

app = FastAPI()
bearer = HTTPBearer()

def verify(token: str) -> dict:
    key = os.environ["JWT_KEY"]
    return jwt.decode(
        token, key, algorithms=["HS256"])
