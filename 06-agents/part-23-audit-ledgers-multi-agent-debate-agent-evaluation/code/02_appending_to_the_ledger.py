"""Zero to AI Engineer · Agents and Tools · Part 23 of 26
Slide: Appending to the ledger
Run: python 02_appending_to_the_ledger.py
"""
def append(ledger, record):
    prev = GENESIS
    if ledger:
        prev = ledger[-1]["hash"]
    # record is nested under its own key,
    # so it cannot override prev or hash
    entry = {"prev": prev, "record": record,
             "hash": _digest(prev, record)}
    ledger.append(entry)
    return entry
