"""Zero to AI Engineer · Production and LLMOps · Part 5 of 38
Slide: The Status Endpoint
Run: python 03_the_status_endpoint.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
# a relay publishes OUTBOX rows to a queue
# at-least-once delivery: idempotent workers
from fastapi import HTTPException
@app.get("/v1/jobs/{job_id}")
async def status_of(job_id: str):
    job = JOBS.get(job_id)
    if job is None:
        raise HTTPException(404, "Unknown job")
    return job
