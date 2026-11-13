"""Zero to AI Engineer · LLM Fundamentals · Part 9 of 18
Slide: Shapes to say in the interview
Run: python 02_shapes_to_say_in_the_interview.py
"""
n, d, V = 5, 8, 50
shapes = [
    ("ids", (n,)),
    ("embeddings", (n, d)),
    ("each block", (n, d)),
    ("final norm", (n, d)),
    ("last position", (d,)),
    ("LM head logits", (V,)),
    ("sample", "one token id"),
]
for name, shape in shapes:
    print(name, shape)
