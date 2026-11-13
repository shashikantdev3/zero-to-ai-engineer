"""Zero to AI Engineer · Python · Part 12 of 25
Slide: Check first versus just try
Run: python 04_check_first_versus_just_try.py
"""
import os

# LBYL: race between check and use
if os.path.exists("cfg.json"):
    pass  # file may vanish here
# EAFP
try:
    with open("cfg.json",
              encoding="utf-8") as f:
        raw = f.read()
except FileNotFoundError:
    raw = "{}"
