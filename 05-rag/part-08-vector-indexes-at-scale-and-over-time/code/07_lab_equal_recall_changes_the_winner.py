"""Zero to AI Engineer · RAG and Vector Search · Part 8 of 26
Follow-along lab: Equal recall changes the winner
Run: python 07_lab_equal_recall_changes_the_winner.py
"""
# recall and p95 ms per knob value
a = {16: (0.88, 2.0), 64: (0.95, 4.0)}
b = {16: (0.80, 1.5), 64: (0.93, 3.0),
     128: (0.96, 6.0)}
def at_target(runs, target=0.95):
    for knob in sorted(runs):
        rec, p95 = runs[knob]
        if rec >= target:
            return knob, p95
print("unfair:", a[16][1], "vs", b[16][1])
print("A at 0.95:", at_target(a))
print("B at 0.95:", at_target(b))
wa, wb = at_target(a)[1], at_target(b)[1]
print("winner:", "A" if wa < wb else "B")
