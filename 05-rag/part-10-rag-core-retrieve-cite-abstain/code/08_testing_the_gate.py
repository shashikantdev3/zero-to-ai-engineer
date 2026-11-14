"""Zero to AI Engineer · RAG and Vector Search · Part 10 of 26
Slide: Testing the gate
Run: python 08_testing_the_gate.py
"""
# --- repeated from 07_gate_on_the_reranker_score.py so this file runs on its own ---
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

# --- this slide ---
hits = [{"id": "a", "@search.score": 0.03,
         "@search.rerankerScore": 3.1}]
print(gate(hits))
print(gate([]))
raw = [{"id": "b", "@search.score": 0.9}]
print(gate(raw))
