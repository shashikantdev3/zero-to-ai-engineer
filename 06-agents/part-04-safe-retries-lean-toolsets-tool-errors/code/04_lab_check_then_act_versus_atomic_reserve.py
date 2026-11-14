"""Zero to AI Engineer · Agents and Tools · Part 4 of 26
Follow-along lab: Check-then-act versus atomic reserve
Run: python 04_lab_check_then_act_versus_atomic_reserve.py
"""
done = []
store = {}
# check-then-act: both retries look first
seen1 = "k" in store
seen2 = "k" in store
if not seen1: done.append("restart")
if not seen2: done.append("restart")
print("check then act:", len(done))
done.clear()
for retry in (1, 2):
    if store.setdefault("k", retry) == retry:
        done.append("restart")
print("atomic reserve:", len(done))
print("owner: retry", store["k"])
