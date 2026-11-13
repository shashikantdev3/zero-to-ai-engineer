"""Zero to AI Engineer · Python · Interview Quiz
Follow-along lab: Flatten, unflatten, round trip
Run: python 04_lab_flatten_unflatten_round_trip.py
"""
def pairs(d, pre=""):
    for k, v in d.items():
        if isinstance(v, dict) and v:
            yield from pairs(v, f"{pre}{k}.")
        else: yield pre + k, v
cfg = {"a": {"b": 1, "c": {}}, "d": 2}
flat = dict(pairs(cfg))
back = {}
for key, v in flat.items():
    *path, last = key.split(".")
    cur = back
    for p in path: cur = cur.setdefault(p, {})
    cur[last] = v
print(flat, back, back == cfg, sep="\n")
