"""Zero to AI Engineer · RAG and Vector Search · Part 8 of 26
Slide: Running the check
Run: python 03_running_the_check.py
"""
# --- repeated from 02_a_scheduled_recall_check.py so this file runs on its own ---
def recall_check(queries, ann, exact,
                 k=10, floor=0.9):
    scores = []
    for q in queries:
        found = set(ann(q, k))
        hits = found & set(exact(q, k))
        scores.append(len(hits) / k)
    recall = sum(scores) / len(scores)
    if recall < floor:
        alert(f"recall fell to {recall:.2f}")
    return recall

# --- this slide ---
def alert(msg):
    print("ALERT:", msg)
# toy searches: ANN misses two neighbours
def exact(q, k):
    return list(range(k))
def ann(q, k):
    return list(range(2, k + 2))
r = recall_check([1, 2, 3], ann, exact)
print(f"recall@10 = {r:.2f}")
