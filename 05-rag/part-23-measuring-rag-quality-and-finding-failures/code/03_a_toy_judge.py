"""Zero to AI Engineer · RAG and Vector Search · Part 23 of 26
Slide: A toy judge
Run: python 03_a_toy_judge.py
"""
class ToyJudge:
    def split_claims(self, text):
        parts = text.split(".")
        return [p.strip() for p in parts
                if p.strip()]

    def is_supported(self, claim, texts):
        low = claim.lower()
        return any(low in t.lower()
                   for t in texts)
