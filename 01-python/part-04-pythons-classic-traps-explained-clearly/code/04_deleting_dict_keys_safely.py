"""Zero to AI Engineer · Python · Part 4 of 25
Slide: Deleting Dict Keys Safely
Run: python 04_deleting_dict_keys_safely.py
"""
d = {"a": 1, "b": 2, "c": 1}
# loop over a snapshot of the keys
for k in list(d):
    if d[k] == 1:
        del d[k]
print(d)
