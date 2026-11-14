"""Zero to AI Engineer · Agents and Tools · Part 7 of 26
Slide: Wiring before_call
Run: python 04_wiring_before_call.py
"""
# --- repeated from 01_the_run_state.py, 02_steps_budget_poll_cap.py, 03_loop_guard_and_counting.py so this file runs on its own ---
import json
from dataclasses import dataclass, field
MAX_STEPS, MAX_USD = 12, 0.05
POLL_TOOLS = {"get_job_status": 10}
class Stop(Exception): pass
# one per run, never module-level
@dataclass
class RunState:
    step: int = 0
    spent_usd: float = 0.0
    last_sig: tuple | None = None
    polls: dict = field(default_factory=dict)

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

def check_repeat(run, name, args):
    parsed = json.loads(args)
    canon = json.dumps(parsed, sort_keys=True)
    sig = (name, canon)
    if sig == run.last_sig:
        raise Stop("same action twice in a row")
    run.last_sig = sig

def after_call(run, actual_usd):
    run.step += 1
    run.spent_usd += actual_usd

# --- this slide ---
def before_call(run, name, args, worst_usd):
    check_limits(run, worst_usd)
    if name in POLL_TOOLS:
        check_poll(run, name)
        return
    check_repeat(run, name, args)

run = RunState()
before_call(run, "search", '{"q": 1}', 0.01)
after_call(run, 0.01)
print(run.step, run.spent_usd)
