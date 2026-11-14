"""Zero to AI Engineer · Production and LLMOps · Part 3 of 38
Follow-along lab: Where the seconds go
Run: python 09_lab_where_the_seconds_go.py
"""
ttft = 0.6
tpot = 0.020

def total(n_tokens):
    return ttft + n_tokens * tpot

full = total(400)
half = total(200)
print(f"Full answer: {full:.1f} s")
print(f"Half answer: {half:.1f} s")
print(f"Saved: {full - half:.1f} s")
print(f"TTFT share: {ttft / full:.0%}")
