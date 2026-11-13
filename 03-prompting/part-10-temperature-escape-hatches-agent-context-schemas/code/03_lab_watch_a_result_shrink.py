"""Zero to AI Engineer · Prompting · Part 10 of 10
Follow-along lab: Watch a result shrink
Run: python 03_lab_watch_a_result_shrink.py
"""
def trim(text, ref, limit=40):
    if len(text) <= limit:
        return text
    return text[:limit] + f" [id={ref}]"

small = "status ok"
big = "row " * 500
print(trim(small, "t1"))
print(len(big), "chars before")
out = trim(big, "t2")
print(len(out), "chars after")
print(out.endswith("[id=t2]"))
