"""Zero to AI Engineer · Security and Guardrails · Part 8 of 11
Slide: Quote checker: the check
Run: python 03_quote_checker_the_check.py
"""
def quote_ok(quote, cited_id, evidence):
    q = norm(quote)
    source = evidence.get(cited_id)
    if source is None:
        return False
    src = norm(source)
    if q not in src:
        return False
    words_ok = len(q.split()) >= MIN_WORDS
    id_ok = bool(ID_PATTERN.match(q))
    rare = src.count(q) <= MAX_OCCURRENCES
    return (words_ok or id_ok) and rare
