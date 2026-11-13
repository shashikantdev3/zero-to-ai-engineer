"""Zero to AI Engineer · Prompting · Part 2 of 10
Slide: One Classifier Call
Run: python 07_one_classifier_call.py
"""
# Needs: pip install anthropic
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
