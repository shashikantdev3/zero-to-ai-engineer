"""Zero to AI Engineer · RAG and Vector Search · Part 2 of 26
Follow-along lab: Lab: Pick a Threshold From Data
Run: python 01_lab_lab_pick_a_threshold_from_data.py
"""
relevant = [0.82, 0.78, 0.74, 0.71, 0.69]
irrelevant = [0.72, 0.66, 0.61, 0.58, 0.55]
tolerance = 0.20
chosen = None
for cut in [0.65, 0.70, 0.75]:
    kept = sum(s >= cut for s in relevant)
    bad = sum(s >= cut for s in irrelevant)
    rate = bad / len(irrelevant)
    msg = f"{cut}: kept {kept}"
    print(msg, f"false {rate:.0%}")
    if chosen is None and rate <= tolerance:
        chosen = cut
print(f"chosen cut: {chosen}")
