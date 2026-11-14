"""Zero to AI Engineer · Security and Guardrails · Part 4 of 11
Slide: Trying three model proposals
Run: python 03_trying_three_model_proposals.py
"""
# --- repeated from 01_sample_orders_and_a_refund_cap.py, 02_the_refund_tool_checks_first.py so this file runs on its own ---
from dataclasses import dataclass

SELF_MAX = 5000

@dataclass
class Order:
    owner: str
    refundable: int
    eligible: bool = True

orders = {"A1": Order("u1", 3000)}

def refund(oid, amount, user_id, intent_id):
    if amount <= 0:
        return "denied: invalid amount"
    order = orders.get(oid)
    if not order or order.owner != user_id:
        return "denied: not your order"
    if not order.eligible:
        return "denied: not eligible"
    cap = min(order.refundable, SELF_MAX)
    if amount > cap:
        return "denied: over limit"
    return f"refund:{oid}:{intent_id}"

# --- this slide ---
import uuid

# the server makes one intent_id per request
intent = uuid.uuid4().hex[:8]
print(refund("A1", 2000, "u1", intent))
print(refund("A1", 2000, "u2", intent))
print(refund("A1", 9000, "u1", intent))
