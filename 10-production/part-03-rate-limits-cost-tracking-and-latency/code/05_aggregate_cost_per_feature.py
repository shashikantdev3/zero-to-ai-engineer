"""Zero to AI Engineer · Production and LLMOps · Part 3 of 38
Slide: Aggregate cost per feature
Run: python 05_aggregate_cost_per_feature.py
"""
# --- repeated from 04_one_record_per_call.py so this file runs on its own ---
from collections import defaultdict

calls = [
    {"cid": "c1", "tenant": "t-17",
     "feature": "triage",
     "model": "claude-haiku-5-5",
     "in": 1840, "cached_in": 1024,
     "out": 212, "usd": 0.0031},
]

# --- this slide ---
calls.append({**calls[0], "cid": "c2",
              "feature": "search",
              "usd": 0.0012})
cost = defaultdict(float)
for c in calls:
    cost[c["feature"]] += c["usd"]
for feature, usd in cost.items():
    print(feature, round(usd, 4))
