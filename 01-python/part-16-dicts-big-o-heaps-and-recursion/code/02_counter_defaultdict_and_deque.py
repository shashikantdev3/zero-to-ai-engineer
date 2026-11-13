"""Zero to AI Engineer · Python · Part 16 of 25
Slide: Counter, defaultdict and deque
Run: python 02_counter_defaultdict_and_deque.py
"""
from collections import Counter, defaultdict
from collections import deque
codes = ["429", "500", "429"]
errors = Counter(codes).most_common(1)
print(errors)  # [('429', 2)]
by_doc = defaultdict(list)
for doc, chunk in [("d1", "a"), ("d1", "b")]:
    by_doc[doc].append(chunk)
# last 3 latencies
window = deque(maxlen=3)
