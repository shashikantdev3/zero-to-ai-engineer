"""Zero to AI Engineer · RAG and Vector Search · Part 16 of 26
Slide: Validate the returned order
Run: python 02_validate_the_returned_order.py
"""
# --- repeated from 01_build_one_prompt_for_the_list.py so this file runs on its own ---
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

# --- this slide ---
def parse_order(out, cands, top=5):
    try:
        ids = [int(x) for x in out.split(",")]
    except ValueError:
        return cands[:top]
    n = len(cands)
    ok = [i for i in ids if 0 <= i < n]
    seen = list(dict.fromkeys(ok))
    rest = [i for i in range(n)
            if i not in seen]
    return [cands[i] for i in seen+rest][:top]
print(parse_order("2, 0, 2, 9", cands))
