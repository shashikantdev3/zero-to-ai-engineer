"""Zero to AI Engineer · Prompting · Part 5 of 10
Follow-along lab: Lab: Trim to a Budget
Run: python 04_lab_lab_trim_to_a_budget.py
"""
n_tok = lambda s: len(s.split())
docs = ["rule " * 40, "ship " * 50,
        "promo " * 80]
fixed = "Answer using the documents."
room = 150 - 40 - n_tok(fixed)
print("room for docs:", room)
kept, used = [], 0
for d in docs:
    t = n_tok(d)
    if used + t > room:
        print("dropped doc of", t, "tokens")
        break
    kept.append(d); used += t
print(f"kept {len(kept)} docs, {used} tok")
