"""Zero to AI Engineer · Evaluation · Part 7 of 11
Slide: A scripted conversation case
Run: python 01_a_scripted_conversation_case.py
"""
turns = [
    ("I am on the London payroll.", None),
    ("When is salary credited?",
     "mentions_location:London"),
    ("And for bonus?",
     "no_contradiction_with_turn:2"),
]
final = {"ticket_raised": False}
CONVO = {"id": "conv-payroll-07",
    "turns": turns, "final_state": final}
# record input tokens per turn too
print(len(CONVO["turns"]), "turns")
