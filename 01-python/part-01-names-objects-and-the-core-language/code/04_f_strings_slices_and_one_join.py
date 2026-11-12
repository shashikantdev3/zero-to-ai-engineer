"""Zero to AI Engineer · Python · Part 1 of 25
Slide: f-strings, slices and one join
Run: python 04_f_strings_slices_and_one_join.py
"""
cost, model = 0.001234, "small"
print(f"{model!r} cost ${cost:.4f}")    # 'small' cost $0.0012
print(f"{cost=}")                        # cost=0.001234  (3.8+)
s = "incident-42"
s[:8], s[-2:], s[::-1], s[100:]          # clipping, no error on s[100:]
prompt = "\n".join(f"[{i}] {c}" for i, c in enumerate(["a", "b"], 1))
