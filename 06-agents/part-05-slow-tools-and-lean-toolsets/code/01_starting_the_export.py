"""Zero to AI Engineer · Agents and Tools · Part 5 of 26
Slide: Starting the export
Run: python 01_starting_the_export.py
"""
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
