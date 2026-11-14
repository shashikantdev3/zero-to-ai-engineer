"""Zero to AI Engineer · Security and Guardrails · Part 5 of 11
Slide: Verify, then mark as used
Run: python 06_verify_then_mark_as_used.py
"""
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
