"""Zero to AI Engineer · Security and Guardrails · Part 3 of 11
Follow-along lab: Build a tiny budget guard
Run: python 03_lab_build_a_tiny_budget_guard.py
"""
BUDGET, PRICE, MAX_IN = 0.01, 1e-6, 5000
spent = 0.0
def guard(in_toks, max_out):
    global spent
    if in_toks > MAX_IN:
        return "too big"
    worst = (in_toks + max_out) * PRICE
    if spent + worst > BUDGET:
        return "blocked"
    spent += worst
    return f"ok, spent {spent:.4f}"
for n in [2000, 3000, 6000, 4800]:
    print(n, guard(n, 300))
