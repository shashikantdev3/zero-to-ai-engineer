"""Zero to AI Engineer · RAG and Vector Search · Part 12 of 26
Follow-along lab: Find the guessing behind a rate
Run: python 05_lab_find_the_guessing_behind_a_rate.py
"""
# each case: (should_answer, refused)
cases = [(True, False)] * 8 + [(True, True)]
cases += [(False, False), (False, False)]
cases += [(False, True)]
refused = sum(r for _, r in cases)
rate = refused / len(cases)
print("refusal rate:", round(rate, 2))
ans = [r for s, r in cases if s]
una = [r for s, r in cases if not s]
print("labelled:", len(ans), "vs", len(una))
fr = sum(ans) / len(ans)
fa = (len(una) - sum(una)) / len(una)
print("false refusal rate:", round(fr, 2))
print("false answer rate:", round(fa, 2))
