"""Zero to AI Engineer · RAG and Vector Search · Part 23 of 26
Follow-along lab: Lab: the blended score trap
Run: python 02_lab_lab_the_blended_score_trap.py
"""
cats = ["answerable"] * 3
cats += ["unanswerable"] * 2
outs = ["30 days.", "Form B.", "Ask HR.",
        "Interns get 10 days.", "Ten days."]
by_cat = {}
for cat, out in zip(cats, outs):
    ok = ("could not find" in out
          if cat == "unanswerable" else True)
    by_cat.setdefault(cat, []).append(ok)
for c, v in by_cat.items():
    print(c, sum(v) / len(v))
flat = sum(by_cat.values(), [])
print("blended", sum(flat) / len(flat))
