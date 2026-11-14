"""Zero to AI Engineer · Production and LLMOps · Part 10 of 38
Slide: Hashing the payload
Run: python 01_hashing_the_payload.py
"""
import hashlib, json

# pending must outlive the downstream timeout
PENDING_TTL = 60
DONE_TTL = 86_400

def payload_hash(payload: dict) -> str:
    canon = json.dumps(
        payload, sort_keys=True,
        separators=(",", ":"))
    return hashlib.sha256(
        canon.encode()).hexdigest()
