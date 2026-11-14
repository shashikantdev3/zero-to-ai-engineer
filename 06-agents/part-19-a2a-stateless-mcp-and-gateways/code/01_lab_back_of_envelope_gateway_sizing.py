"""Zero to AI Engineer · Agents and Tools · Part 19 of 26
Follow-along lab: Back-of-envelope gateway sizing
Run: python 01_lab_back_of_envelope_gateway_sizing.py
"""
# Gateway sizing, back of envelope
per_hour = 5_000_000
avg_rps = per_hour / 3600
print(f"average rps: {avg_rps:.0f}")
peak_rps = avg_rps * 3
print(f"peak rps: {peak_rps:.0f}")
# Little's law: rate x p95 latency
rate, p95 = 500, 0.2
print(f"connections: {rate * p95:.0f}")
# Cache key must include the tenant
cache = {("tenant_a", "v2"): ["search"]}
print(("tenant_b", "v2") in cache)
