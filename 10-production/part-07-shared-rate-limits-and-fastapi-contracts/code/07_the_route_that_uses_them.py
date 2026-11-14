"""Zero to AI Engineer · Production and LLMOps · Part 7 of 38
Slide: The route that uses them
Run: python 07_the_route_that_uses_them.py
"""
# Needs: pip install fastapi pydantic
# (not run while building this repo, because the package was not installed there)
# --- repeated from 06_the_request_and_response_models.py so this file runs on its own ---
from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel, Field

class AskIn(BaseModel):
    question: str = Field(min_length=1,
                          max_length=4_000)

class AskOut(BaseModel):
    answer: str
    citations: list[str]

app = FastAPI()

# --- this slide ---
async def current_user() -> dict:
    return {"tid": "tenant-a"}
@app.post("/v1/ask", response_model=AskOut)
async def ask(
    body: AskIn,
    user=Depends(current_user),
    top_k: int = Query(5, ge=1, le=20),
):
    # from the verified token, never the URL
    tenant_id = user["tid"]
    return {"answer": "ok", "citations": [],
            "cost": 0.02, "tid": tenant_id}
