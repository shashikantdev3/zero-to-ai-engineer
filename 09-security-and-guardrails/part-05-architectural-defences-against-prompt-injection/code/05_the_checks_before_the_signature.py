"""Zero to AI Engineer · Security and Guardrails · Part 5 of 11
Slide: The checks before the signature
Run: python 05_the_checks_before_the_signature.py
"""
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
