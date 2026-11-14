"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 1 of 10
Follow-along lab: See Which Tokens Get Graded
Run: python 04_lab_see_which_tokens_get_graded.py
"""
chat = [("system", "Be brief."),
        ("user", "Capital of France?"),
        ("assistant", "Paris.")]
text, mask = [], []
for role, words in chat:
    for tok in [f"<{role}>"] + words.split():
        text.append(tok)
        mask.append(role == "assistant")
print("tokens:", len(text))
graded = [t for t, m in zip(text, mask) if m]
print("graded:", graded)
print("masked:", mask.count(False))
share = len(graded) / len(text)
print(f"graded share: {share:.0%}")
