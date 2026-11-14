"""Zero to AI Engineer · Agents and Tools · Part 8 of 26
Follow-along lab: Measure pass^k from replays
Run: python 02_lab_measure_pass_k_from_replays.py
"""
runs = {
    "refund": [1, 1, 1, 0, 1, 1, 1, 1],
    "address": [1, 1, 1, 1, 1, 1, 1, 1],
    "cancel": [1, 0, 1, 1, 0, 1, 1, 1],
}
for task, tries in runs.items():
    print(task, "all 8 passed:", all(tries))
flat = [r for t in runs.values() for r in t]
p1 = sum(flat) / len(flat)
print(f"pass^1 = {p1:.2f}")
ok = sum(all(t) for t in runs.values())
print(f"pass^8 = {ok / len(runs):.2f}")
