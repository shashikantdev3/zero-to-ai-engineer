"""Zero to AI Engineer · Production and LLMOps · Part 10 of 38
Slide: PUT to a client-chosen ID
Run: python 07_put_to_a_client_chosen_id.py
"""
# Needs: pip install fastapi pydantic
# (not run while building this repo, because the package was not installed there)
# --- repeated from 06_a_retry_safe_create_setup.py so this file runs on its own ---
from fastapi import FastAPI, Response, status
from pydantic import BaseModel

app = FastAPI()

class TicketIn(BaseModel):
    title: str

# --- this slide ---
# the client picks the ID
@app.put("/v1/tickets/{ticket_id}")
async def upsert_ticket(ticket_id: str,
                        body: TicketIn,
                        response: Response):
    # same ID twice = same state
    created = await repo.upsert(
        ticket_id, body)
    response.status_code = (
        status.HTTP_201_CREATED if created
        else status.HTTP_200_OK)
    return {"id": ticket_id}
