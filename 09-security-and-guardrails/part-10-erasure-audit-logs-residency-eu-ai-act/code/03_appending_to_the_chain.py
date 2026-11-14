"""Zero to AI Engineer · Security and Guardrails · Part 10 of 11
Slide: Appending to the Chain
Run: python 03_appending_to_the_chain.py
"""
# --- repeated from 02_hashing_one_log_entry.py so this file runs on its own ---
import hashlib, json
ZERO = "0" * 64

def _hash(prev: str, event: dict) -> str:
    body = json.dumps(event, sort_keys=True,
                      separators=(",", ":"))
    return hashlib.sha256(
        (prev + body).encode()).hexdigest()

# --- this slide ---
def append(log: list, event: dict) -> dict:
    prev = log[-1]["hash"] if log else ZERO
    entry = {"prev": prev, "event": event,
             "hash": _hash(prev, event)}
    log.append(entry)
    return entry

chain = []
append(chain, {"who": "u1", "act": "ask"})
append(chain, {"who": "bot", "act": "reply"})
