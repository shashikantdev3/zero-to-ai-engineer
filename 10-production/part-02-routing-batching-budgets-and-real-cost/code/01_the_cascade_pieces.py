"""Zero to AI Engineer · Production and LLMOps · Part 2 of 38
Slide: The cascade pieces
Run: python 01_the_cascade_pieces.py
"""
RULES = {"reset password": "Use the link."}

def small_model(req):
    return {"answer": "Refunds take 5 days",
            "quote": "refunds take 5 days"}

def large_model(req):
    return {"answer": "Large model answer"}

def validate(out, doc):
    q = out.get("quote")
    return bool(q) and q in doc
