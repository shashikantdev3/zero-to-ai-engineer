"""Zero to AI Engineer · Evaluation · Part 10 of 11
Slide: The verify loop
Run: python 07_the_verify_loop.py
"""
def verify(claims, chunks, judge):
    src = fmt(chunks)
    kept, dropped = [], []
    for claim in claims:
        reply = judge(VERIFY.format(
            sources=src, claim=claim))
        ids = parse_ids(reply.strip())
        if ids and ids <= set(chunks):
            kept.append((claim, sorted(ids)))
        else:
            dropped.append(claim)
    return kept, dropped
