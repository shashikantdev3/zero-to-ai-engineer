"""Zero to AI Engineer · LLM Fundamentals · Part 14 of 18
Slide: Greedy Versus Beam, Offline
Run: python 01_greedy_versus_beam_offline.py
"""
# step 1 options, then step 2 options
P = {"the": 0.6, "a": 0.4}
NEXT = {"the": {"cat": 0.5, "dog": 0.5},
        "a": {"cat": 0.9, "dog": 0.1}}
# greedy: top token at each step
w1 = max(P, key=P.get)
w2 = max(NEXT[w1], key=NEXT[w1].get)
print("greedy:", w1, w2, P[w1] * NEXT[w1][w2])
# beam: keep both starts, score whole pairs
pairs = [(P[a] * NEXT[a][b], a, b)
         for a in P for b in NEXT[a]]
print("beam:", max(pairs))
