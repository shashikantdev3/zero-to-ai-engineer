"""Zero to AI Engineer · Agents and Tools · Part 6 of 26
Follow-along lab: Lab: step limit and loop guard
Run: python 04_lab_lab_step_limit_and_loop_guard.py
"""
def agent(script, max_steps=4):
    seen = set()
    steps = script[:max_steps]
    for n, act in enumerate(steps, 1):
        if act == "done":
            return f"finished at step {n}"
        if act in seen:
            return f"loop guard at step {n}"
        seen.add(act)
    return f"step limit after {max_steps}"

print(agent(["search", "read", "done"]))
print(agent(["search", "search"]))
print(agent(["a", "b", "c", "d", "e"]))
