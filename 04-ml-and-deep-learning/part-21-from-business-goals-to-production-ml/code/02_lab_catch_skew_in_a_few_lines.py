"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 21 of 28
Follow-along lab: Catch skew in a few lines
Run: python 02_lab_catch_skew_in_a_few_lines.py
"""
rows = [{"age": 31}, {"age": None}, {"age": 52}]
def serve(r):
    a = r["age"]
    return 0 if a is None else a
def train(r):
    a = r["age"]
    return 40 if a is None else a
print("Same name:", "age" == "age")
diffs = [serve(r) != train(r) for r in rows]
print("Rows compared:", len(rows))
print("Rows that disagree:", sum(diffs))
share = round(sum(diffs) / len(rows), 2)
print("Share:", share)
