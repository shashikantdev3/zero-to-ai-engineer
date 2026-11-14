"""Zero to AI Engineer · RAG and Vector Search · Part 14 of 26
Slide: BM25 in a few lines
Run: python 04_bm25_in_a_few_lines.py
"""
# Needs: pip install rank_bm25
from rank_bm25 import BM25Okapi
docs = ["VPN error E4410 on login",
        "Time off and leave policy",
        "Reset your VPN password"]
# lowercase, then split on spaces
tokens = [d.lower().split() for d in docs]
bm25 = BM25Okapi(tokens)
query = "error e4410 vpn".split()
scores = bm25.get_scores(query)
print(scores)
