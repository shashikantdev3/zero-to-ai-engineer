"""Zero to AI Engineer · LLM Fundamentals · Part 3 of 18
Follow-along lab: Count a pasted email's cost
Run: python 05_lab_count_a_pasted_emails_cost.py
"""
EMAIL_TOKENS = 3000
history = []
billed = 0
for turn in range(1, 5):
    msg = "email" if turn == 1 else "ask"
    history.append(msg)
    # every call resends the whole history
    sent = history.count("email") * EMAIL_TOKENS
    billed += sent
    print(f"turn {turn}: {sent} email tokens")
print(f"email billed: {billed} tokens")
