"""Zero to AI Engineer · Evaluation · Part 1 of 11
Follow-along lab: Lab: redact before you save
Run: python 04_lab_lab_redact_before_you_save.py
"""
import re
EMAIL = re.compile(
    r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE = re.compile(r"\+?\d[\d\s-]{8,}\d")

def redact(text):
    text = EMAIL.sub("[EMAIL]", text)
    return PHONE.sub("[PHONE]", text)

print(redact("Mail user@example.com re leave"))
print(redact("Call +44 7700 900123 now"))
print(redact("Bonus for 2023?"))
