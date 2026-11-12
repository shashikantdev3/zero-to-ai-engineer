"""Zero to AI Engineer · Python · Part 2 of 25
Slide: Unpack, Merge, Read in Blocks
Run: python 03_unpack_merge_read_in_blocks.py
"""
import io

first, *rest = ["plan", "act", "check"]
base = {"temperature": 0.2}
new = {"temperature": 0.0, "max_tokens": 200}
# right side wins: temperature is 0.0
cfg = base | new

f = io.BytesIO(b"x" * 20000)
while (block := f.read(8192)):
    print(len(block))
