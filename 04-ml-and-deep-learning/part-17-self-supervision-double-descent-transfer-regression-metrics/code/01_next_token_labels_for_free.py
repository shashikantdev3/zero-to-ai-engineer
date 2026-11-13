"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 17 of 28
Slide: Next-Token Labels for Free
Run: python 01_next_token_labels_for_free.py
"""
tokens = [101, 7, 42, 9, 13]
# next-token labels for free
inputs = tokens[:-1]
targets = tokens[1:]
for x, y in zip(inputs, targets):
    print(x, "->", y)
