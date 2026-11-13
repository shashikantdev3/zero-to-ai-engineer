"""Zero to AI Engineer · Prompting · Part 2 of 10
Follow-along lab: Vote, Then Check the Truth
Run: python 09_lab_vote_then_check_the_truth.py
"""
from collections import Counter
runs = {
    "noisy": ["network", "access", "network",
              "other", "network"],
    "stable": ["other"] * 5,
}
for name, answers in runs.items():
    top = Counter(answers).most_common(1)
    label, votes = top[0]
    act = "auto" if votes >= 4 else "human"
    print(f"{name}: {label} {votes}/5 {act}")
    print(f"  correct: {label == 'network'}")
