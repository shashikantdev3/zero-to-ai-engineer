"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 5 of 10
Slide: The cascade itself
Run: python 04_the_cascade_itself.py
"""
# --- repeated from 03_stand_in_models_and_a_check.py so this file runs on its own ---
import json
def small_model(req):
    if "disk" in req:
        return '{"label": "storage"}'
    return "I am very confident."
def big_model(req):
    return '{"label": "escalated"}'
def passes_checks(out):
    try:
        return "label" in json.loads(out)
    except json.JSONDecodeError:
        return False

# --- this slide ---
def answer(req):
    out = small_model(req)
    # schema, rules, quoted evidence
    if passes_checks(out):
        return out, "small"
    return big_model(req), "big"

print(answer("disk full on db-01"))
print(answer("odd login errors"))
