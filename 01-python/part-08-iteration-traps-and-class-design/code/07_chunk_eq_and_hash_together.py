"""Zero to AI Engineer · Python · Part 8 of 25
Slide: Chunk: eq and hash together
Run: python 07_chunk_eq_and_hash_together.py
"""
class Chunk:
    def __init__(self, doc_id, text):
        self.doc_id, self.text = doc_id, text
    def _key(self):
        return (self.doc_id, self.text)
    def __eq__(self, o):
        return (isinstance(o, Chunk)
                and self._key() == o._key())
    def __hash__(self):
        return hash(self._key())

print(Chunk("d1", "hi") == Chunk("d1", "hi"))
