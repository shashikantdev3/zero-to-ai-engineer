"""Zero to AI Engineer · Production and LLMOps · Part 8 of 38
Follow-along lab: See offset pages break
Run: python 14_lab_see_offset_pages_break.py
"""
rows = list(range(100, 0, -1))
# newest first: 100, 99, 98, ...
page1 = rows[0:3]
print("page 1:", page1)
# a new row arrives at the top
rows.insert(0, 101)
by_offset = rows[3:6]
print("offset page 2:", by_offset)
dup = set(page1) & set(by_offset)
print("repeated:", dup)
last = page1[-1]
by_cursor = [r for r in rows if r < last][:3]
print("cursor page 2:", by_cursor)
