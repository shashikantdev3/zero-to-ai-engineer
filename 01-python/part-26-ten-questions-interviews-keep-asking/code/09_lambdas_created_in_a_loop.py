"""Zero to AI Engineer · Python · Interview Quiz
Slide: Lambdas created in a loop
Run: python 09_lambdas_created_in_a_loop.py
"""
fns = []
for i in range(3):
    fns.append(lambda: i)
print([f() for f in fns])
