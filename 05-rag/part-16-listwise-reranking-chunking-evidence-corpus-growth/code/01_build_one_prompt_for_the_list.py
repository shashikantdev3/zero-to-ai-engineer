"""Zero to AI Engineer · RAG and Vector Search · Part 16 of 26
Slide: Build one prompt for the list
Run: python 01_build_one_prompt_for_the_list.py
"""
def build_prompt(query, cands):
    listing = "\n".join(
        f"[{i}] {c[:500]}"
        for i, c in enumerate(cands))
    return (f"Query: {query}\n"
        "Rank the passages by relevance. "
        "Return ids only, comma separated.\n"
        + listing)
cands = ["refunds", "hours", "refund form"]
q = "how do I get a refund"
print(build_prompt(q, cands))
