"""Zero to AI Engineer · Evaluation · Part 10 of 11
Slide: A triage function
Run: python 01_a_triage_function.py
"""
def triage(trace, expected_ids):
    # chunks actually sent, after rerank
    # and truncation
    sent = {c["chunk_id"]
            for c in trace["final_context"]}
    if not (sent & set(expected_ids)):
        return "retrieval_failure"
    return "generation_failure"

ctx = [{"chunk_id": "c7"}]
trace = {"final_context": ctx}
print(triage(trace, ["c2"]))
