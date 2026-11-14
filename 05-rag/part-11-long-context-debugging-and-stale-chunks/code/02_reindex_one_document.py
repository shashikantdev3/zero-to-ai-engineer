"""Zero to AI Engineer · RAG and Vector Search · Part 11 of 26
Slide: Reindex One Document
Run: python 02_reindex_one_document.py
"""
# --- repeated from 01_a_tiny_stand_in_index.py so this file runs on its own ---
class Index:
    def __init__(self):
        self.db = {}
    def upsert(self, chunks):
        for c in chunks:
            self.db[c["id"]] = c
    def ids_for(self, doc_id):
        return [i for i, c in self.db.items()
                if c["doc"] == doc_id]
    def delete(self, ids):
        for i in ids:
            del self.db[i]

# --- this slide ---
def reindex(index, doc_id, new_chunks):
    new_ids = {c["id"] for c in new_chunks}
    # write the new version first
    index.upsert(new_chunks)
    old = set(index.ids_for(doc_id))
    stale = old - new_ids
    if stale:
        # then remove leftovers
        index.delete(list(stale))
idx = Index()
idx.upsert([{"id": "a", "doc": "p"}])
reindex(idx, "p", [{"id": "b", "doc": "p"}])
