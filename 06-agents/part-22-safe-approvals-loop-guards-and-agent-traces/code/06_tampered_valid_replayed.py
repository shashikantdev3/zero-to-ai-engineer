"""Zero to AI Engineer · Agents and Tools · Part 22 of 26
Slide: Tampered, valid, replayed
Run: python 06_tampered_valid_replayed.py
"""
# Needs: pip install cryptography
# --- repeated from 01_the_approval_message.py, 02_the_console_signs.py, 03_who_may_approve_this_plan.py, 04_rebuild_the_message_then_verify.py, 05_expiry_and_a_one_time_nonce.py so this file runs on its own ---
import hashlib, json

def canonical(obj) -> bytes:
    # stable in one Python service only
    return json.dumps(obj, sort_keys=True,
        separators=(",", ":")).encode()

def approval_msg(inc, plan, meta):
    data = canonical(plan)
    h = hashlib.sha256(data).hexdigest()
    return canonical({"incident": inc,
        "plan_sha256": h, **meta})

import secrets, time
from cryptography.hazmat.primitives \
    .asymmetric import ed25519
# approval console: the only private key
priv = ed25519.Ed25519PrivateKey.generate()
plan = {"target": "db", "risk_tier": 2}
meta = {"approver": "ops-lead",
        "exp": int(time.time()) + 900,
        "nonce": secrets.token_hex(16)}
msg = approval_msg("INC-1", plan, meta)
sig = priv.sign(msg)

PUBKEYS = {"ops-lead": priv.public_key()}
REVOKED = set()
ROLES = {("ops-lead", "db"): 2}
def authorised(who, requester, plan):
    if who not in PUBKEYS or who in REVOKED:
        return False
    # segregation of duties
    if who == requester:
        return False
    svc = plan["target"]
    return plan["risk_tier"] <= ROLES.get(
        (who, svc), 0)

from cryptography.exceptions import (
    InvalidSignature)
def verify(meta, sig, inc, run_plan, req):
    who = meta["approver"]
    if not authorised(who, req, run_plan):
        return False
    msg = approval_msg(inc, run_plan, meta)
    try:
        PUBKEYS[who].verify(sig, msg)
        return True
    except InvalidSignature:
        return False

USED = set()
def execute_ok(meta, sig, inc, plan, req):
    if not verify(meta, sig, inc, plan, req):
        return False
    if time.time() > meta["exp"]:
        return False
    if meta["nonce"] in USED:
        return False
    # production: atomic insert, durable store
    USED.add(meta["nonce"])
    return True

# --- this slide ---
req = "dev-1"
changed = {"target": "db", "risk_tier": 1}
print(execute_ok(meta, sig, "INC-1",
                 changed, req))
print(execute_ok(meta, sig, "INC-1",
                 plan, req))
print(execute_ok(meta, sig, "INC-1",
                 plan, req))
