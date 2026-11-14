"""Zero to AI Engineer · Agents and Tools · Part 7 of 26
Follow-along lab: Watch the rules fire
Run: python 05_lab_watch_the_rules_fire.py
"""
import json
def run(acts, limit=4, step=0, last=None):
    for t, a in acts:
        if step >= limit:
            return f"stop: step limit at {step}"
        k = (t, json.dumps(a, sort_keys=True))
        if k == last and t != "poll":
            return f"stop: repeat at step {step}"
        last, step = k, step + 1
    return f"done after {step} steps"
x, y = {"a": 1, "b": 2}, {"b": 2, "a": 1}
print(run([("read", x), ("read", y)]))
print(run([("poll", x)] * 3))
print(run([("poll", x)] * 6))
