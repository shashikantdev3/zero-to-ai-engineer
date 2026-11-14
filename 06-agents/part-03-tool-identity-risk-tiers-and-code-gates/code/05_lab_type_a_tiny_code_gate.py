"""Zero to AI Engineer · Agents and Tools · Part 3 of 26
Follow-along lab: Type a tiny code gate
Run: python 05_lab_type_a_tiny_code_gate.py
"""
ALLOWED = {"track": {"get_order"},
           "refund": {"get_order", "refund"}}
orders = {("A1", "u1"): 48_000}
def gate(intent, oid, amt, uid):
    cap = orders.get((oid, uid))
    if "refund" not in ALLOWED[intent]:
        return "reject: not allowed"
    if cap is None: return "reject: no order"
    if not 0 < amt <= min(cap, 50_000):
        return "reject: over limit"
    return "ok: send to human"
print(gate("track", "A1", 48_000, "u1"))
print(gate("refund", "A1", 60_000, "u1"))
print(gate("refund", "A1", 48_000, "u1"))
