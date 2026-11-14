"""Zero to AI Engineer · Production and LLMOps · Part 10 of 38
Slide: A retry-safe create: setup
Run: python 06_a_retry_safe_create_setup.py
"""
# Needs: pip install fastapi pydantic
# (not run while building this repo, because the package was not installed there)
from fastapi import FastAPI, Response, status
from pydantic import BaseModel

app = FastAPI()

class TicketIn(BaseModel):
    title: str
