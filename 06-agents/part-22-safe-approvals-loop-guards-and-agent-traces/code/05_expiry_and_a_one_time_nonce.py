"""Zero to AI Engineer · Agents and Tools · Part 22 of 26
Slide: Expiry and a one-time nonce
Run: python 05_expiry_and_a_one_time_nonce.py
"""
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
