"""Zero to AI Engineer · RAG and Vector Search · Part 10 of 26
Slide: Retrieval with a permission filter
Run: python 01_retrieval_with_a_permission_filter.py
"""
THRESHOLD = 0.5
REFUSAL = "I do not know. Open a ticket?"
DOCS = [("leave-policy-2026#s3-c2",
         "Staff get 25 days of leave.", "hr")]

def retrieve(q, groups):
    # permission filter first
    hits = [(c, t, 0.9) for c, t, g in DOCS
            if g in groups]
    # rerank stand-in: best score first
    hits.sort(key=lambda h: -h[2])
    return hits[:5]
