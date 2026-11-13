"""Zero to AI Engineer · Prompting · Part 2 of 10
Slide: Sending the Examples
Run: python 02_sending_the_examples.py
"""
# Needs: pip install anthropic
# --- repeated from 01_building_few_shot_messages.py so this file runs on its own ---
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

# --- this slide ---
import anthropic
client = anthropic.Anthropic()
few_shot = [
    user("cant login to vpn since mornng"),
    bot("network", "cant login to vpn"),
    user("pls order cake for team"),
    bot("other", "order cake"),
]
resp = client.messages.create(
    model="claude-haiku-5-5", max_tokens=200,
    thinking={"type": "disabled"},
    system=SYSTEM,
    messages=few_shot + [user("wifi down")])
