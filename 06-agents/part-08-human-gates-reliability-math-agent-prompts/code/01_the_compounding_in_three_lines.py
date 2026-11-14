"""Zero to AI Engineer · Agents and Tools · Part 8 of 26
Slide: The compounding in three lines
Run: python 01_the_compounding_in_three_lines.py
"""
per_step = 0.95
steps = 20
# whole task, if errors were independent
print(round(per_step ** steps, 3))
# a more reliable step
print(round(0.99 ** steps, 3))
# one step moved from the model into code
print(round(per_step ** (steps - 1), 3))
