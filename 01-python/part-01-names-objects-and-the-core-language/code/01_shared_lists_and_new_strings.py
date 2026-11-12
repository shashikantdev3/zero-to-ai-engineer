"""Zero to AI Engineer · Python · Part 1 of 25
Slide: Shared lists and new strings
Run: python 01_shared_lists_and_new_strings.py
"""
a = [1, 2]
b = a
b.append(3)
print(a)            # [1, 2, 3], same object
s = "abc"
t = s.upper()       # new object, s unchanged
hash((1, 2))        # fine
# hash((1, [2]))    # TypeError: unhashable type: 'list'
