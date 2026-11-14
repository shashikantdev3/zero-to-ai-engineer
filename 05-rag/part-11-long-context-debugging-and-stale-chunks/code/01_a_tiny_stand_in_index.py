"""Zero to AI Engineer · RAG and Vector Search · Part 11 of 26
Slide: A Tiny Stand-In Index
Run: python 01_a_tiny_stand_in_index.py
"""
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
