"""Zero to AI Engineer · Prompting · Part 2 of 10
Slide: Building Few-Shot Messages
Run: python 01_building_few_shot_messages.py
"""
import json
SYSTEM = "Classify IT tickets as JSON."
def user(text):
    msg = f"<ticket>{text}</ticket>"
    return {"role": "user", "content": msg}
def bot(cat, why):
    out = json.dumps({"category": cat,
                      "reason": why})
    return {"role": "assistant",
            "content": out}
