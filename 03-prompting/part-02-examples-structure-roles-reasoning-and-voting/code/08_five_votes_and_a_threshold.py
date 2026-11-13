"""Zero to AI Engineer · Prompting · Part 2 of 10
Slide: Five Votes and a Threshold
Run: python 08_five_votes_and_a_threshold.py
"""
# --- repeated from 07_one_classifier_call.py so this file runs on its own ---
from collections import Counter
import anthropic
client = anthropic.Anthropic()
SYS = "Label this IT ticket in one word."
def classify(t):
    r = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=10,
        thinking={"type": "disabled"},
        system=SYS,
        messages=[{"role": "user",
                   "content": t}])
    return r.content[0].text.strip()

# --- this slide ---
# no temperature passed; runs still vary
ticket = "cant reach shared drive from home"
answers = [classify(ticket) for _ in range(5)]
top = Counter(answers).most_common(1)
label, votes = top[0]
if votes < 4:
    print("route to human:", answers)
else:
    print("auto label:", label)
