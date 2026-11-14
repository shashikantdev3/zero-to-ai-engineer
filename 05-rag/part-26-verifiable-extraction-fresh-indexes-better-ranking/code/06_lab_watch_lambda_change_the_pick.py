"""Zero to AI Engineer · RAG and Vector Search · Part 26 of 26
Follow-along lab: Watch lambda change the pick
Run: python 06_lab_watch_lambda_change_the_pick.py
"""
rel = {"A": 0.95, "A2": 0.94, "B": 0.80}
# similarity to A, the doc already picked
sim_a = {"A2": 0.99, "B": 0.30}

def mmr_score(d, lam):
    return lam * rel[d] - (1 - lam) * sim_a[d]

print("first pick: A (most relevant)")
for lam in (1.0, 0.7, 0.5):
    a2 = mmr_score("A2", lam)
    b = mmr_score("B", lam)
    best = "A2" if a2 > b else "B"
    msg = f"A2 {a2:.3f} B {b:.3f}"
    print(f"lam {lam}: {msg} -> {best}")
