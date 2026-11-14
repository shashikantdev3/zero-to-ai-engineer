"""Zero to AI Engineer · Production and LLMOps · Part 2 of 38
Follow-along lab: Check after versus reserve first
Run: python 05_lab_check_after_versus_reserve_first.py
"""
# money in cents keeps the maths exact
LIMIT, WORST, ACTUAL = 100, 10, 8
# check after: all 20 workers see 0 spent
passed = [0 < LIMIT for _ in range(20)]
print("all passed:", all(passed))
print("spent, cents:", len(passed) * ACTUAL)
# reserve first: hold the worst case
held = ok = 0
for _ in range(20):
    if held + WORST <= LIMIT:
        held += WORST
        ok += 1
print("calls allowed:", ok)
print("max spend, cents:", ok * ACTUAL)
