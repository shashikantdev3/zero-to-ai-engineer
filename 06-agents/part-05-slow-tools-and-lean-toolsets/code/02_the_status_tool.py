"""Zero to AI Engineer · Agents and Tools · Part 5 of 26
Slide: The status tool
Run: python 02_the_status_tool.py
"""
# --- repeated from 01_starting_the_export.py so this file runs on its own ---
import time
jobs = {}

def start_export(inc, service, hours):
    # 15-minute time bucket
    bucket = int(time.time() // 900)
    # key scopes one intended export
    idem = f"{inc}:{service}:{hours}:{bucket}"
    if idem not in jobs:
        jobs[idem] = f"job-{len(jobs) + 1}"
    return {"job_id": jobs[idem],
            "status": "running"}

# --- this slide ---
status = {}
def get_job_status(job_id):
    # status, later a short summary
    state = status.get(job_id, "running")
    return {"job_id": job_id, "status": state}

a = start_export("INC-1", "api", 2)
b = start_export("INC-1", "api", 2)
c = start_export("INC-2", "api", 2)
print(a["job_id"], b["job_id"], c["job_id"])
print(get_job_status(a["job_id"]))
