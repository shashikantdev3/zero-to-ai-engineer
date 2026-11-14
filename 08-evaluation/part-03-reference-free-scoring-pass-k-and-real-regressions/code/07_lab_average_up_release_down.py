"""Zero to AI Engineer · Evaluation · Part 3 of 11
Follow-along lab: Average up, release down
Run: python 07_lab_average_up_release_down.py
"""
old = {"q1": 1, "q2": 0, "q3": 0, "q4": 1}
new = {"q1": 0, "q2": 1, "q3": 1, "q4": 1}
critical = {"q1"}
avg_old = sum(old.values()) / len(old)
avg_new = sum(new.values()) / len(new)
print("old average:", avg_old)
print("new average:", avg_new)
broke = [c for c in old if old[c] > new[c]]
fixed = [c for c in old if old[c] < new[c]]
print("broke:", broke)
print("fixed:", fixed)
block = [c for c in broke if c in critical]
print("ship?", "NO" if block else "yes")
