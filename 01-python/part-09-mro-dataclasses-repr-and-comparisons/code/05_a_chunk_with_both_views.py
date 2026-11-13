"""Zero to AI Engineer · Python · Part 9 of 25
Slide: A chunk with both views
Run: python 05_a_chunk_with_both_views.py
"""
class Chunk:
    def __init__(self, doc_id, text):
        self.doc_id, self.text = doc_id, text
    def __repr__(self):
        d, n = self.doc_id, len(self.text)
        return (f"Chunk(doc_id={d!r}, "
                f"chars={n})")
    def __str__(self):
        return self.text[:40]
c = Chunk("d1", "Leave is twenty days.")
print(c)
print([c])
