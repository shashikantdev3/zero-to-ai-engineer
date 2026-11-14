"""Zero to AI Engineer · Agents and Tools · Part 23 of 26
Slide: Hashing one entry
Run: python 01_hashing_one_entry.py
"""
import hashlib
import json

GENESIS = "0" * 64

def _digest(prev, record):
    body = json.dumps(
        {"prev": prev, "record": record},
        sort_keys=True, separators=(",", ":"),
        default=str)
    data = body.encode()
    return hashlib.sha256(data).hexdigest()
