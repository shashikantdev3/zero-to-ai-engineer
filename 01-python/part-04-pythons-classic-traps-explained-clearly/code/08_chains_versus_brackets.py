"""Zero to AI Engineer · Python · Part 4 of 25
Slide: Chains Versus Brackets
Run: python 08_chains_versus_brackets.py
"""
x = 5
print(0 < x < 10)
# (False == False) and (False in [False])
print(False == False in [False])
# brackets change the meaning
print((False == False) in [False])
