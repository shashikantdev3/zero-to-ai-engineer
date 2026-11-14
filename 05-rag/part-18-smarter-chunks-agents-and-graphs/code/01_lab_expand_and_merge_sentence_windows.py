"""Zero to AI Engineer · RAG and Vector Search · Part 18 of 26
Follow-along lab: Expand and merge sentence windows
Run: python 01_lab_expand_and_merge_sentence_windows.py
"""
sents = [f"S{i}" for i in range(10)]
hits = [2, 3, 8]
N = 2
win = []
for h in hits:
    lo, hi = max(0, h - N), min(9, h + N)
    if win and lo <= win[-1][1]:
        win[-1][1] = max(win[-1][1], hi)
    else:
        win.append([lo, hi])
print("hits:", hits)
for lo, hi in win:
    print(lo, hi, " ".join(sents[lo:hi + 1]))
print("vectors stored:", len(sents))
