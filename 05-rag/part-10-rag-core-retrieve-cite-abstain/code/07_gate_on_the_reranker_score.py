"""Zero to AI Engineer · RAG and Vector Search · Part 10 of 26
Slide: Gate on the reranker score
Run: python 07_gate_on_the_reranker_score.py
"""
# set from labelled data, not guessed
MIN_SCORE = 2.0
REFUSAL = "I do not know. Open a ticket?"
def gate(results):
    top = results[0] if results else None
    # fixed documented scale; check the docs
    score = (top.get("@search.rerankerScore")
             if top else None)
    # never threshold @search.score from RRF
    if score is None or score < MIN_SCORE:
        return REFUSAL
    return "answer from " + top["id"]
