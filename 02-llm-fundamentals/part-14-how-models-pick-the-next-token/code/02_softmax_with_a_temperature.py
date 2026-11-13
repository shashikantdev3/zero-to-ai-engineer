"""Zero to AI Engineer · LLM Fundamentals · Part 14 of 18
Slide: Softmax With a Temperature
Run: python 02_softmax_with_a_temperature.py
"""
import math
def softmax_t(logits, t=1.0):
    if t == 0:
        # greedy: all probability on the argmax
        top = logits.index(max(logits))
        return [float(i == top)
                for i in range(len(logits))]
    z = [x / t for x in logits]
    m = max(z)
    # subtract max or tiny t overflows exp
    e = [math.exp(x - m) for x in z]
    return [x / sum(e) for x in e]
