"""Zero to AI Engineer · RAG and Vector Search · Part 13 of 26
Slide: Stand ins for store and cache
Run: python 03_stand_ins_for_store_and_cache.py
"""
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
