"""Zero to AI Engineer · LLM Fundamentals · Part 12 of 18
Follow-along lab: Watch Image Tokens Grow
Run: python 04_lab_watch_image_tokens_grow.py
"""
def patches(w, h, p=16):
    return (w // p) * (h // p)

sizes = [(224, 224), (448, 448), (896, 896)]
for w, h in sizes:
    print(w, "px:", patches(w, h), "tokens")
small = patches(224, 224)
big = patches(448, 448)
print("ratio:", big // small)
