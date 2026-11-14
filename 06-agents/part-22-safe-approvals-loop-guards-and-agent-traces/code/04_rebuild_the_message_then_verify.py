"""Zero to AI Engineer · Agents and Tools · Part 22 of 26
Slide: Rebuild the message, then verify
Run: python 04_rebuild_the_message_then_verify.py
"""
# Needs: pip install cryptography
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
