"""Zero to AI Engineer · Production and LLMOps · Part 1 of 38
Follow-along lab: Watch history get billed again
Run: python 04_lab_watch_history_get_billed_again.py
"""
# one long email, then three short turns
turns = [3_000, 50, 40, 60]
history = 0
billed = 0
for n, t in enumerate(turns, start=1):
    history += t
    billed += history
    print(f"turn {n}: sent {history} tokens")
print(f"total billed: {billed} tokens")
