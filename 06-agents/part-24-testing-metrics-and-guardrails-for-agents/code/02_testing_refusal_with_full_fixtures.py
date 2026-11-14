"""Zero to AI Engineer · Agents and Tools · Part 24 of 26
Slide: Testing refusal with full fixtures
Run: python 02_testing_refusal_with_full_fixtures.py
"""
def verify(meta, sig, requester):
    if not sig:
        return False
    if meta["approver"] == requester:
        return False
    return True

# explicit fixture: every field present
meta = {"approver": "rev1", "exp": 0,
        "nonce": "n"}
assert verify(meta, b"", "req1") is False
assert verify(meta, b"sig", "rev1") is False
