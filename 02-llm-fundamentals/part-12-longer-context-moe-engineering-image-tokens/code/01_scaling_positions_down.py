"""Zero to AI Engineer · LLM Fundamentals · Part 12 of 18
Slide: Scaling Positions Down
Run: python 01_scaling_positions_down.py
"""
trained = 4096
target = 16384
factor = target / trained
# config entry; field names vary by version
rope_scaling = {"factor": factor}
# interpolation: scale positions down
pos = 12000
scaled = pos / factor
print(rope_scaling)
print(scaled, "<", trained)
