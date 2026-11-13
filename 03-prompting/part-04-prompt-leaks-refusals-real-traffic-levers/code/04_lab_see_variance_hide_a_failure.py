"""Zero to AI Engineer · Prompting · Part 4 of 10
Follow-along lab: See Variance Hide a Failure
Run: python 04_lab_see_variance_hide_a_failure.py
"""
# Five runs per case, scores fixed for demo
SCORES = {
    "tidy": [1, 1, 1, 1, 1],
    "typos": [1, 1, 0, 1, 1],
    "pasted": [1, 0, 1, 0, 1],
}
print("one run only:", SCORES["typos"][0])
for case, runs in SCORES.items():
    m = sum(runs) / len(runs)
    w = min(runs)
    print(f"{case}: mean {m} worst {w}")
