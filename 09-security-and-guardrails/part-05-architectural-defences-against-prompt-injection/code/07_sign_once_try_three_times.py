"""Zero to AI Engineer · Security and Guardrails · Part 5 of 11
Slide: Sign once, try three times
Run: python 07_sign_once_try_three_times.py
"""
# Needs: pip install cryptography
# --- repeated from 04_canonical_bytes_and_known_keys.py, 05_the_checks_before_the_signature.py, 06_verify_then_mark_as_used.py so this file runs on its own ---
import hashlib, json, time
from cryptography import exceptions
from cryptography.hazmat.primitives \
    .asymmetric import ed25519
def canonical(obj) -> bytes:
    return json.dumps(obj, sort_keys=True,
        separators=(",", ":")).encode()
# Demo only: the console holds this key
sk = ed25519.Ed25519PrivateKey.generate()
APPROVERS = {"k1": sk.public_key()}
REVOKED, USED = set(), set()

def checks_pass(a, inc, plan, req):
    k = a.get("approver_key_id")
    if k not in APPROVERS or k in REVOKED:
        return False
    if k == req or a["incident_id"] != inc:
        return False
    h = hashlib.sha256(canonical(plan))
    if a["plan_hash"] != h.hexdigest():
        return False
    if time.time() > a["expires_at"] + 30:
        return False
    return a["approval_id"] not in USED

def approved(a, sig, inc, plan, req):
    if not checks_pass(a, inc, plan, req):
        return False
    try:
        key = APPROVERS[a["approver_key_id"]]
        key.verify(sig, canonical(a))
    except exceptions.InvalidSignature:
        return False
    USED.add(a["approval_id"])
    return True

# --- this slide ---
plan = {"action": "restart", "risk_tier": 2}
a = {"approver_key_id": "k1",
     "incident_id": "INC-7",
     "plan_hash": hashlib.sha256(
         canonical(plan)).hexdigest(),
     "expires_at": time.time() + 300,
     "approval_id": "ap-1"}
sig = sk.sign(canonical(a))
bad = dict(plan, action="delete")
print(approved(a, sig, "INC-7", bad, "k2"))
print(approved(a, sig, "INC-7", plan, "k2"))
print(approved(a, sig, "INC-7", plan, "k2"))
