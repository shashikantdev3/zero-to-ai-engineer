"""Zero to AI Engineer · RAG and Vector Search · Part 13 of 26
Slide: A deletion check for nightly runs
Run: python 04_a_deletion_check_for_nightly_runs.py
"""
# --- repeated from 03_stand_ins_for_store_and_cache.py so this file runs on its own ---
class Store:
    def __init__(self, ids):
        self.ids = ids
    def count(self, filter):
        key = filter["doc_id"]
        return self.ids.count(key)

class Cache:
    def __init__(self, ids):
        self.ids = ids
    def has_entries_for(self, doc_id):
        return doc_id in self.ids

# --- this slide ---
def assert_erased(doc_id, store, cache):
    q = {"doc_id": doc_id}
    assert store.count(filter=q) == 0
    assert not cache.has_entries_for(doc_id)

store = Store(["doc-9"])
cache = Cache([])
assert_erased("doc-7", store, cache)
print("doc-7 fully erased")
