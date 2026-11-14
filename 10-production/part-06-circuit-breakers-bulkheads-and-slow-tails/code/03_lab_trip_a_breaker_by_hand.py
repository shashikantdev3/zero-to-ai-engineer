"""Zero to AI Engineer · Production and LLMOps · Part 6 of 38
Follow-along lab: Trip a breaker by hand
Run: python 03_lab_trip_a_breaker_by_hand.py
"""
st = {"fails": 0, "at": None}
def allow(t):
    a = st["at"]
    return a is None or t - a >= 30
def record(ok, t):
    st["fails"] = 0 if ok else st["fails"] + 1
    if ok or st["fails"] >= 3:
        st["at"] = None if ok else t
print("t=0 allowed:", allow(0))
for t in (0, 1, 2): record(False, t)
print("t=2 allowed:", allow(2))
print("t=40 probe allowed:", allow(40))
record(True, 40)
print("closed again:", st["at"] is None)
