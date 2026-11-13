"""Zero to AI Engineer · Python · Part 9 of 25
Follow-along lab: Prove what a dataclass checks
Run: python 04_lab_prove_what_a_dataclass_checks.py
"""
from dataclasses import dataclass, field
from dataclasses import FrozenInstanceError
@dataclass(frozen=True, slots=True)
class Retry:
    attempts: int = 5
@dataclass
class Bag:
    t: list = field(default_factory=list)
r = Retry(attempts="five")
print("accepted:", r.attempts)
try: r.attempts = 9
except FrozenInstanceError: print("blocked")
a, b = Bag(), Bag(); a.t.append("x")
print("a:", a.t, "b:", b.t)
