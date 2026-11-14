"""Zero to AI Engineer · RAG and Vector Search · Part 3 of 26
Slide: Recall at k in four lines
Run: python 02_recall_at_k_in_four_lines.py
"""
def ann_recall_at_k(ann_ids, exact_ids, k=10):
    found = set(ann_ids[:k])
    truth = set(exact_ids[:k])
    return len(found & truth) / k

exact = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ann = [1, 2, 3, 4, 5, 6, 7, 8, 9, 42]
print(ann_recall_at_k(ann, exact))
