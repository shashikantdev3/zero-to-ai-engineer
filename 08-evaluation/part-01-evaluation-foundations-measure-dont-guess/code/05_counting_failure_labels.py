"""Zero to AI Engineer · Evaluation · Part 1 of 11
Slide: Counting failure labels
Run: python 05_counting_failure_labels.py
"""
from collections import Counter
labels = ["missing_doc",
          "ignored_context",
          "missing_doc", "stale_doc",
          "format"]
# fix the top category first
print(Counter(labels).most_common())
