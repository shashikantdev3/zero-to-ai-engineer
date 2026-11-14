"""Zero to AI Engineer · Agents and Tools · Part 7 of 26
Slide: Steps, budget, poll cap
Run: python 02_steps_budget_poll_cap.py
"""
def check_limits(run, worst_usd):
    if run.step >= MAX_STEPS:
        raise Stop("step limit")
    if run.spent_usd + worst_usd > MAX_USD:
        raise Stop("budget")

def check_poll(run, name):
    n = run.polls.get(name, 0) + 1
    run.polls[name] = n
    if n > POLL_TOOLS[name]:
        raise Stop(f"poll cap for {name}")
