"""Zero to AI Engineer · Python · Part 8 of 25
Slide: Chunk: init, repr, len
Run: python 06_chunk_init_repr_len.py
"""
class Chunk:
    def __init__(self, doc_id, text):
        self.doc_id, self.text = doc_id, text
    def __repr__(self):
        d, n = self.doc_id, len(self.text)
        return f"Chunk({d!r}, {n} chars)"
    def __len__(self):
        return len(self.text)

c = Chunk("d1", "hello")
print(c, len(c))
