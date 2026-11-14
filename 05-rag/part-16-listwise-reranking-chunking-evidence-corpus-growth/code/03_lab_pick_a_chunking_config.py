"""Zero to AI Engineer · RAG and Vector Search · Part 16 of 26
Follow-along lab: Pick a chunking config
Run: python 03_lab_pick_a_chunking_config.py
"""
scores = {
    (256, 0, "recursive"): 71.2,
    (256, 50, "recursive"): 70.4,
    (512, 0, "structure"): 72.0,
    (512, 50, "structure"): 71.6,
}
print("configs tried:", len(scores))
best = max(scores.values())
print("best MRR:", best)
ok = [k for k, v in scores.items()
      if v >= best - 1]
print("within one point:", len(ok))
pick = min(ok)
print("pick:", pick)
