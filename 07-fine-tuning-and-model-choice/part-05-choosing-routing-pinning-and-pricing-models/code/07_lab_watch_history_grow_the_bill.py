"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 5 of 10
Follow-along lab: Watch history grow the bill
Run: python 07_lab_watch_history_grow_the_bill.py
"""
P_IN, P_OUT = 0.15, 0.60
SYSTEM = 500
turn_in, turn_out = 200, 300
history = 0
total = 0.0
for turn in range(1, 4):
    tin = SYSTEM + history + turn_in
    c = tin * P_IN + turn_out * P_OUT
    total += c / 1e6
    history += turn_in + turn_out
    print(f"turn {turn}: {tin} input tokens")
print(f"3 turns cost ${total:.6f}")
