"""Zero to AI Engineer · Security and Guardrails · Part 4 of 11
Slide: The refund tool checks first
Run: python 02_the_refund_tool_checks_first.py
"""
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
