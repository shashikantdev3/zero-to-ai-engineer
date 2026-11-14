"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 8 of 10
Follow-along lab: Simulate static versus continuous
Run: python 02_lab_simulate_static_versus_continuous.py
"""
lengths = [10, 1000, 12, 8]
t, static = 0, []
for i in range(0, 4, 2):
    batch = lengths[i:i + 2]
    static += [t + n for n in batch]
    t += max(batch)
ends, cont = [0, 0], []
for n in lengths:
    s = ends.index(min(ends))
    ends[s] += n
    cont.append(ends[s])
print("static:", static)
print("continuous:", cont)
print("request 3 saved:", static[2] - cont[2])
