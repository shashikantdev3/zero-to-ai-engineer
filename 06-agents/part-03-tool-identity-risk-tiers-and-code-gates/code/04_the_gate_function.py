"""Zero to AI Engineer · Agents and Tools · Part 3 of 26
Slide: The gate function
Run: python 04_the_gate_function.py
"""
def gate(intent, tool, args, uid):
    if tool not in ALLOWED.get(intent, set()):
        return False, f"{tool} not allowed"
    if tool == "propose_refund":
        order = orders.get(args.order_id)
        if not order or order.owner != uid:
            return False, "order not found"
        limit = min(order.refundable_inr,
                    POLICY_MAX_INR)
        if not 0 < args.amount_inr <= limit:
            return False, "amount over limit"
    return True, "ok"
