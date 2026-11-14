"""Zero to AI Engineer · Agents and Tools · Part 22 of 26
Slide: Who may approve this plan?
Run: python 03_who_may_approve_this_plan.py
"""
# Needs: pip install cryptography
# --- repeated from 01_the_approval_message.py, 02_the_console_signs.py so this file runs on its own ---
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

# --- this slide ---
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
