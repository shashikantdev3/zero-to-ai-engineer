"""Zero to AI Engineer · Production and LLMOps · Part 10 of 38
Slide: One answer: missing or forbidden
Run: python 08_one_answer_missing_or_forbidden.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
from fastapi import HTTPException

async def get_ticket_for(user, ticket_id):
    # scoped query: only this tenant's rows
    t = await repo.get(ticket_id,
                       tenant_id=user["tid"])
    if t is None:
        # same answer: missing or not yours
        raise HTTPException(404, "Not found")
    return t
