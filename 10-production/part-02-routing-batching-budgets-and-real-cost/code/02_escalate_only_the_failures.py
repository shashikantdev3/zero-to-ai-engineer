"""Zero to AI Engineer · Production and LLMOps · Part 2 of 38
Slide: Escalate only the failures
Run: python 02_escalate_only_the_failures.py
"""
# --- repeated from 01_the_cascade_pieces.py so this file runs on its own ---
RULES = {"reset password": "Use the link."}

def small_model(req):
    return {"answer": "Refunds take 5 days",
            "quote": "refunds take 5 days"}

def large_model(req):
    return {"answer": "Large model answer"}

def validate(out, doc):
    q = out.get("quote")
    return bool(q) and q in doc

# --- this slide ---
def answer(req, doc):
    if req in RULES:
        # zero tokens spent
        return RULES[req]
    out = small_model(req)
    if validate(out, doc):
        return out["answer"]
    # escalate only the failures
    return large_model(req)["answer"]

doc = "Note: refunds take 5 days."
print(answer("refund status", doc))
