"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 12 of 28
Slide: The posterior in code
Run: python 01_the_posterior_in_code.py
"""
def posterior(prev, sens=0.99, spec=0.99):
    # true positives: sick and caught
    hit = sens * prev
    # false alarms from the healthy group
    alarm = (1 - spec) * (1 - prev)
    # law of total probability: P(positive)
    return hit / (hit + alarm)

# about 0.0098, roughly 1 in 102
print(posterior(1 / 10_000))
# about 0.92
print(posterior(1 / 10))
