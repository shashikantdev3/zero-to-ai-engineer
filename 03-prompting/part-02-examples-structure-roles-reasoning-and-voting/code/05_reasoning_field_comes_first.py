"""Zero to AI Engineer · Prompting · Part 2 of 10
Slide: Reasoning Field Comes First
Run: python 05_reasoning_field_comes_first.py
"""
import json, anthropic
client = anthropic.Anthropic()
LABELS = ["access", "hardware", "software",
          "network", "other"]
# reasoning first: generated first
schema = {"type": "object",
    "properties": {
        "reasoning": {"type": "string"},
        "category": {"type": "string",
                     "enum": LABELS}},
    "required": ["reasoning", "category"],
    "additionalProperties": False}
