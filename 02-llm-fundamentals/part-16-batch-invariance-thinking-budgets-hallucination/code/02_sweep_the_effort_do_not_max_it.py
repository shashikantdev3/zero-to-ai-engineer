"""Zero to AI Engineer · LLM Fundamentals · Part 16 of 18
Slide: Sweep the effort, do not max it
Run: python 02_sweep_the_effort_do_not_max_it.py
"""
def run_eval(cases, reasoning_effort):
    # stub with made-up numbers
    table = {"low": (0.81, 2.1, 0.40),
             "medium": (0.88, 4.0, 0.90),
             "high": (0.87, 9.5, 2.20)}
    return table[reasoning_effort]
cases = []
for effort in ("low", "medium", "high"):
    acc, p95, cost = run_eval(cases, effort)
    print(effort, acc, p95, cost)
# pick the lowest effort that clears the bar
