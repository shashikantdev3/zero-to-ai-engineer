"""Zero to AI Engineer · Agents and Tools · Part 5 of 26
Follow-along lab: Test the idempotency key
Run: python 03_lab_test_the_idempotency_key.py
"""
def start(jobs, key):
    if key not in jobs:
        jobs[key] = f"job-{len(jobs) + 1}"
    return jobs[key]

g = {}
print("first:", start(g, "I1:api:2:5"))
print("retry:", start(g, "I1:api:2:5"))
print("incident 2:", start(g, "I2:api:2:5"))
print("next bucket:", start(g, "I1:api:2:6"))
# key without incident: I2 reuses I1
b = {}
start(b, "api:2")
print("I2, bad key:", start(b, "api:2"))
