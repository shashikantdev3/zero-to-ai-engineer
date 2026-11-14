"""Zero to AI Engineer · Evaluation · Part 10 of 11
Slide: A narrow judge prompt
Run: python 05_a_narrow_judge_prompt.py
"""
VERIFY = """Sources (ID in brackets):
{sources}

Claim: {claim}
A claim may be supported by several
sources together. Reply on one line with
bare IDs, no brackets, e.g.: SUPPORTED c1, c3
or reply: NOT_SUPPORTED"""

def fmt(chunks):
    return "\n\n".join(f"[{k}] {t}"
        for k, t in chunks.items())
