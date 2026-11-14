"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 5 of 10
Slide: Stand-in models and a check
Run: python 03_stand_in_models_and_a_check.py
"""
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
