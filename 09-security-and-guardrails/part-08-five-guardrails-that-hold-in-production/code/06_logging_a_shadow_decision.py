"""Zero to AI Engineer · Security and Guardrails · Part 8 of 11
Slide: Logging a shadow decision
Run: python 06_logging_a_shadow_decision.py
"""
import logging
log = logging.getLogger("guards")
reply, req_id, live = "Thanks", "r1", False
def new_guard_check(text):
    return {"block": True, "category": "Hate"}
decision = new_guard_check(reply)
log.info("guard_shadow", extra={
    "would_block": decision["block"],
    "category": decision["category"],
    "live_blocked": live, "req": req_id})
# enforce only the live guard until
# shadow metrics are reviewed
