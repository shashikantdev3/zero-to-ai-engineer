"""Zero to AI Engineer · Python · Part 8 of 25
Slide: Mutate versus rebind
Run: python 02_mutate_versus_rebind.py
"""
data = [1, 2, 3]
g = (x for x in data)
data.append(4)
# same list, mutated: [1, 2, 3, 4]
print(list(g))

data = [1, 2, 3]
g = (x for x in data)
data = [9]
# rebinding is not seen: [1, 2, 3]
print(list(g))
