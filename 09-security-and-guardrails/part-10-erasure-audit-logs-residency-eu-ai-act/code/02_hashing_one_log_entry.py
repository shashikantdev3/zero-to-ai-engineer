"""Zero to AI Engineer · Security and Guardrails · Part 10 of 11
Slide: Hashing One Log Entry
Run: python 02_hashing_one_log_entry.py
"""
import hashlib, json
ZERO = "0" * 64

def _hash(prev: str, event: dict) -> str:
    body = json.dumps(event, sort_keys=True,
                      separators=(",", ":"))
    return hashlib.sha256(
        (prev + body).encode()).hexdigest()
