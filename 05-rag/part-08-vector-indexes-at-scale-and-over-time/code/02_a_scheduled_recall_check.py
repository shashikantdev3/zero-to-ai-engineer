"""Zero to AI Engineer · RAG and Vector Search · Part 8 of 26
Slide: A scheduled recall check
Run: python 02_a_scheduled_recall_check.py
"""
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
