"""Zero to AI Engineer · RAG and Vector Search · Part 17 of 26
Slide: A parent store and child hits
Run: python 11_a_parent_store_and_child_hits.py
"""
parent_store = {
    "sec-1": "Leave rule, then its exception.",
    "sec-2": "Contractor terms section.",
}

def search(query, k=20):
    # stand-in: ranked child chunks
    ids = ["sec-1", "sec-1", "sec-2"]
    return [{"metadata": {"parent_id": i}}
            for i in ids][:k]
