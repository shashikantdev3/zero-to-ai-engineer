"""Zero to AI Engineer · LLM Fundamentals · Part 15 of 18
Follow-along lab: Watch a Rounding Error Flip a Token
Run: python 04_lab_watch_a_rounding_error_flip_a_token.py
"""
# same three numbers, two addition orders
s1 = (0.1 + 0.2) + 0.3
s2 = 0.1 + (0.2 + 0.3)
print("order A:", s1)
print("order B:", s2)
print("equal:", s1 == s2)
# a rival token scores exactly 0.6
rival = 0.6
pick_a = "cat" if s1 > rival else "dog"
pick_b = "cat" if s2 > rival else "dog"
print("greedy pick A:", pick_a)
print("greedy pick B:", pick_b)
