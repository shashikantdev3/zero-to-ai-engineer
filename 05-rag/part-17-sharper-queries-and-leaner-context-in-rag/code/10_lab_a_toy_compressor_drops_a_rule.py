"""Zero to AI Engineer · RAG and Vector Search · Part 17 of 26
Follow-along lab: A toy compressor drops a rule
Run: python 10_lab_a_toy_compressor_drops_a_rule.py
"""
q = {"parental", "leave", "contractor"}
chunk = [
    "parental leave covers each contractor.",
    "the office cafe opens at nine.",
    "exception: not during probation.",
]
kept = [s for s in chunk
        if q & set(s.rstrip(".").split())]
print("sentences before:", len(chunk))
print("sentences after:", len(kept))
print("cafe kept:", chunk[1] in kept)
print("exception kept:", chunk[2] in kept)
