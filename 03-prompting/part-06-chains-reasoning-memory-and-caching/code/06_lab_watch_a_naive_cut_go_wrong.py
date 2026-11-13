"""Zero to AI Engineer · Prompting · Part 6 of 10
Follow-along lab: Watch a naive cut go wrong
Run: python 06_lab_watch_a_naive_cut_go_wrong.py
"""
h = "u a u call result a u a".split()
keep = 4
naive = len(h) - keep
print("naive cut starts at:", h[naive])
print("naive keeps:", " ".join(h[naive:]))
cut = naive
# step back to a clean user turn
while cut > 0 and h[cut] != "u":
    cut -= 1
print("safe cut starts at:", h[cut])
print("kept:", " ".join(h[cut:]))
print("summarised:", cut, "turns")
