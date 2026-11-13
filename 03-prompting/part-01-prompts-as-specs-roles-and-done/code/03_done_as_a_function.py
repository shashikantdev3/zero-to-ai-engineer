"""Zero to AI Engineer · Prompting · Part 1 of 10
Slide: Done as a Function
Run: python 03_done_as_a_function.py
"""
def is_done(ans: dict, ids: set[str]) -> bool:
    text = ans.get("text") or ""
    if len(text.split()) > 120:
        return False
    cites = ans.get("citations") or []
    if ans["status"] == "not_found":
        # a not-found answer cites nothing
        return len(cites) == 0
    # at least one valid citation
    ok = all(c in ids for c in cites)
    return bool(cites) and ok
