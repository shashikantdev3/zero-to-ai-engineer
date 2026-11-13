"""Zero to AI Engineer · Prompting · Part 9 of 10
Slide: Truth check one: the totals
Run: python 08_truth_check_one_the_totals.py
"""
import re
from decimal import Decimal, InvalidOperation
NUMBER = re.compile(r"\d[\d,]*(?:\.\d+)?")
PRE = r"(?<![A-Za-z0-9])"
POST = r"(?![A-Za-z0-9])"

def semantic_problems(inv):
    lines = sum(l.amount for l in inv.lines)
    gap = abs(lines + inv.tax - inv.total)
    if gap > Decimal("0.01"):
        return ["lines + tax != total"]
    return []
