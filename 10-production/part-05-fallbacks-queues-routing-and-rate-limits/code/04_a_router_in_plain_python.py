"""Zero to AI Engineer · Production and LLMOps · Part 5 of 38
Slide: A Router in Plain Python
Run: python 04_a_router_in_plain_python.py
"""
def route(intent: str, complexity: float):
    if intent in ("status", "hours"):
        return "rules"
    # threshold tuned offline on evals
    if complexity < 0.4:
        return "small"
    return "large"

print(route("hours", 0.9))
print(route("refund", 0.2))
print(route("refund", 0.7))
