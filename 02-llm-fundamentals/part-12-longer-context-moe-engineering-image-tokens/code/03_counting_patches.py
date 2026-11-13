"""Zero to AI Engineer · LLM Fundamentals · Part 12 of 18
Slide: Counting Patches
Run: python 03_counting_patches.py
"""
def patches(w, h, p=16):
    return (w // p) * (h // p)

print(patches(224, 224))
print(patches(448, 448))
