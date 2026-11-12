"""Zero to AI Engineer · Python · Part 4 of 25
Slide: The Silent List Skip
Run: python 05_the_silent_list_skip.py
"""
xs = [1, 1, 2, 3]
for x in xs:
    if x == 1:
        xs.remove(x)
# one 1 was skipped, no error
print(xs)
# correct: build a new list
ys = [x for x in [1, 1, 2, 3] if x != 1]
print(ys)
