"""Zero to AI Engineer · Production and LLMOps · Part 5 of 38
Slide: Accept the Job, Return 202
Run: python 02_accept_the_job_return_202.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
import uuid
from fastapi import FastAPI, Response
app = FastAPI()
JOBS, OUTBOX = {}, []
@app.post("/v1/jobs", status_code=202)
async def submit(response: Response):
    job_id = uuid.uuid4().hex
    JOBS[job_id] = {"status": "pending"}
    OUTBOX.append((job_id, "cid-1"))
    loc = f"/v1/jobs/{job_id}"
    response.headers["Location"] = loc
    return {"job_id": job_id}
