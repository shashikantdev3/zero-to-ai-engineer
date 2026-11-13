"""Zero to AI Engineer · Prompting · Part 9 of 10
Follow-along lab: Lab: value, boundary, totals
Run: python 11_lab_lab_value_boundary_totals.py
"""
import re
from decimal import Decimal

a = Decimal("1,250.00".replace(",", ""))
print("value match:", a == Decimal("1250.0"))
print("string match:", "1,250.00" == "1250.0")
pat = r"(?<![A-Za-z0-9])12(?![A-Za-z0-9])"
for doc in ["INV-1234", "Ref 12 paid"]:
    hit = bool(re.search(pat, doc))
    print(f"12 in {doc}: {hit}")
lines = [Decimal("100"), Decimal("50")]
gap = sum(lines) + Decimal("15") - 170
ok = abs(gap) <= Decimal("0.01")
print("totals ok:", ok)
