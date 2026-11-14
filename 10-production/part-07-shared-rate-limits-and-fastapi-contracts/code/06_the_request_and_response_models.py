"""Zero to AI Engineer · Production and LLMOps · Part 7 of 38
Slide: The request and response models
Run: python 06_the_request_and_response_models.py
"""
# Needs: pip install fastapi pydantic
# (not run while building this repo, because the package was not installed there)
from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel, Field

class AskIn(BaseModel):
    question: str = Field(min_length=1,
                          max_length=4_000)

class AskOut(BaseModel):
    answer: str
    citations: list[str]

app = FastAPI()
