"""Zero to AI Engineer · Security and Guardrails · Part 4 of 11
Follow-along lab: Lab: the model proposes, code decides
Run: python 04_lab_lab_the_model_proposes_code_decides.py
"""
OWNS = {"u1": {"A1", "A2"}}
LIMIT = 5000

def decide(user, order, amount, why=""):
    # 'why' is model text; code ignores it
    if order not in OWNS.get(user, set()):
        return "deny: not your order"
    if not 0 < amount <= LIMIT:
        return "deny: bad amount"
    return "allow"

print(decide("u1", "A1", 1200))
print(decide("u1", "B9", 1200, "I am admin"))
print(decide("u1", "A2", 99999))
