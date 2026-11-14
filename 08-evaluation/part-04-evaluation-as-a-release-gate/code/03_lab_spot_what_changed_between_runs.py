"""Zero to AI Engineer · Evaluation · Part 4 of 11
Follow-along lab: Spot what changed between runs
Run: python 03_lab_spot_what_changed_between_runs.py
"""
import hashlib

def sha(text):
    h = hashlib.sha256(text.encode())
    return h.hexdigest()[:7]
old = {"prompt": sha("Answer politely."),
       "model": "model-2026-01-15",
       "judge": sha("Rubric v1")}
new = dict(old, judge=sha("Rubric v2"))
for key, value in old.items():
    same = value == new[key]
    print(key, "same" if same else "CHANGED")
if old["judge"] != new["judge"]:
    print("Judge changed: rescore baseline")
