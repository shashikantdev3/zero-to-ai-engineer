"""Zero to AI Engineer · Python · Part 2 of 25
Slide: Strict zip and Empty Checks
Run: python 02_strict_zip_and_empty_checks.py
"""
inputs = ["q1", "q2"]
outputs = ["a1", "a2"]
# raises ValueError if lengths differ
pairs = list(zip(inputs, outputs,
                 strict=True))
checks = []
# True, careful
print(all(checks))
# False
print(any(checks))
