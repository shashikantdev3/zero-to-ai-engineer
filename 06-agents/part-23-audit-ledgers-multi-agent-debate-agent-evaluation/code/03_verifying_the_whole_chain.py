"""Zero to AI Engineer · Agents and Tools · Part 23 of 26
Slide: Verifying the whole chain
Run: python 03_verifying_the_whole_chain.py
"""
def verify(ledger):
    prev = GENESIS
    for e in ledger:
        if e["prev"] != prev:
            return False
        want = _digest(prev, e["record"])
        if e["hash"] != want:
            return False
        prev = e["hash"]
    return True
