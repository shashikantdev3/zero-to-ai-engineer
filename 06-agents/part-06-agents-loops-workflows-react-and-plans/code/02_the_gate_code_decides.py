"""Zero to AI Engineer · Agents and Tools · Part 6 of 26
Slide: The gate: code decides
Run: python 02_the_gate_code_decides.py
"""
ALLOWED = {"lookup"}
def gate(c):
    return c.name in ALLOWED and "id" in c.input
def handle(calls):
    res = []
    for c in calls:
        out = "error: BLOCKED"
        if gate(c):
            out = f"{c.input['id']}: shipped"
        res.append({"type": "tool_result",
        "tool_use_id": c.id, "content": out})
    return res
