"""Zero to AI Engineer · Agents and Tools · Part 1 of 26
Slide: Treat arguments as untrusted
Run: python 03_treat_arguments_as_untrusted.py
"""
import json, re
# in production: from the verified token
user_id = "u-42"
def get_order(order_id, user_id):
    return {"ok": True, "status": "shipped"}
def run_call(b):
    # arguments are untrusted input
    oid = str(b.input.get("order_id", ""))
    if not re.fullmatch(r"ORD-\d{6}", oid):
        return {"ok": False,
                "error": "INVALID_ARGS"}
    return get_order(oid, user_id=user_id)
