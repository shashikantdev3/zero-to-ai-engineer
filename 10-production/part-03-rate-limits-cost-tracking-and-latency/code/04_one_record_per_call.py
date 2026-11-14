"""Zero to AI Engineer · Production and LLMOps · Part 3 of 38
Slide: One record per call
Run: python 04_one_record_per_call.py
"""
from collections import defaultdict

calls = [
    {"cid": "c1", "tenant": "t-17",
     "feature": "triage",
     "model": "claude-haiku-5-5",
     "in": 1840, "cached_in": 1024,
     "out": 212, "usd": 0.0031},
]
