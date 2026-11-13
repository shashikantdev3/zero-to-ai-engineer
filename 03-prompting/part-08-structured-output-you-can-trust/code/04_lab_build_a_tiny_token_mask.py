"""Zero to AI Engineer · Prompting · Part 8 of 10
Follow-along lab: Build a tiny token mask
Run: python 04_lab_build_a_tiny_token_mask.py
"""
scores = {"Sure": 9, "[": 5,
          "true": 4, "]": 2}
grammar = [["["], ["true", "false"], ["]"]]
out = []
for step, allowed in enumerate(grammar, 1):
    best = max(scores, key=scores.get)
    ok = {t: s for t, s in scores.items()
          if t in allowed}
    pick = max(ok, key=ok.get)
    out.append(pick)
    print(step, "wants", best, "gets", pick)
print("output:", "".join(out))
