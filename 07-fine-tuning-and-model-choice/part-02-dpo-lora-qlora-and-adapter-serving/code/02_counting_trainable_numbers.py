"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 2 of 10
Slide: Counting trainable numbers
Run: python 02_counting_trainable_numbers.py
"""
# trainable params per adapted matrix
d, k, r = 4096, 4096, 8
lora = r * (d + k)
full = d * k
print(lora, full)
print(round(100 * lora / full, 2), "percent")
