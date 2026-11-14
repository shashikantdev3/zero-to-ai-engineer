"""Zero to AI Engineer · RAG and Vector Search · Part 17 of 26
Slide: From children to parents
Run: python 12_from_children_to_parents.py
"""
# --- repeated from 11_a_parent_store_and_child_hits.py so this file runs on its own ---
parent_store = {
    "sec-1": "Leave rule, then its exception.",
    "sec-2": "Contractor terms section.",
}

def search(query, k=20):
    # stand-in: ranked child chunks
    ids = ["sec-1", "sec-1", "sec-2"]
    return [{"metadata": {"parent_id": i}}
            for i in ids][:k]

# --- this slide ---
query = "Can contractors take parental leave?"
child_hits = search(query, k=20)
parent_ids = list(dict.fromkeys(
    h["metadata"]["parent_id"]
    for h in child_hits))
parents = [parent_store[pid]
           for pid in parent_ids[:4]]
print(parent_ids)
print(len(parents), "parents sent")
