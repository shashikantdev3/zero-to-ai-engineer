"""Zero to AI Engineer · Python · Part 4 of 25
Slide: Watch the Error and the Change
Run: python 07_watch_the_error_and_the_change.py
"""
t = (1, [2])
try:
    t[1] += [3]
except TypeError as e:
    print(e)
print(t)
# no assignment step, so no error
t[1].extend([4])
print(t)
