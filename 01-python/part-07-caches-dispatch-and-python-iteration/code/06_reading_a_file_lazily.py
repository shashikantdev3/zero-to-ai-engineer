"""Zero to AI Engineer · Python · Part 7 of 25
Slide: Reading a file lazily
Run: python 06_reading_a_file_lazily.py
"""
import json

def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)
