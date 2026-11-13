"""Zero to AI Engineer · Python · Part 24 of 25
Follow-along lab: Lab: count across shards
Run: python 06_lab_lab_count_across_shards.py
"""
import re
from collections import Counter
EMAIL = re.compile(
    r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
def count(lines):
    return Counter(m.lower() for ln in lines
                   for m in EMAIL.findall(ln))
s1 = count(["Ann@x.io and bo@y.io."])
s2 = count(["ann@x.io", "no address"])
total = Counter()
for c in (s1, s2): total.update(c)
print(EMAIL.findall("bo@y.io."))
print(total.most_common(1))
print("distinct:", len(total))
