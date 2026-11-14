"""Zero to AI Engineer · Agents and Tools · Part 12 of 26
Follow-along lab: Crash, resume, pay only once
Run: python 03_lab_crash_resume_pay_only_once.py
"""
runs, sent, saved = [], set(), {}
def pay(key, crash):
    runs.append(key)
    sent.add(key)
    if crash:
        raise RuntimeError("crash")
    saved["paid"] = True
try: pay("inc-4711", crash=True)
except RuntimeError:
    print("crashed, saved:", saved)
pay("inc-4711", crash=False)
print("node ran", len(runs), "times")
print("payments sent:", len(sent))
print("saved:", saved)
