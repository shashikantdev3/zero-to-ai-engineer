"""Zero to AI Engineer · Python · Part 1 of 25
Follow-along lab: See shared objects with your eyes
Run: python 02_lab_see_shared_objects_with_your_eyes.py
"""
a = [1, 2]
b = a
b.append(3)
print("a is now", a)
s = "abc"
t = s.upper()
print(s, t)
pair = (1, [2])
pair[1].append(3)
print(pair)
try:
    hash(pair)
except TypeError as err:
    print("TypeError:", err)
