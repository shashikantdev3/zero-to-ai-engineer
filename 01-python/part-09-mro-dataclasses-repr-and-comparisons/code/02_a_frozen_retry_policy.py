"""Zero to AI Engineer · Python · Part 9 of 25
Slide: A frozen retry policy
Run: python 02_a_frozen_retry_policy.py
"""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class RetryPolicy:
    attempts: int = 5
    base: float = 0.5
    cap: float = 20.0

p = RetryPolicy()
# p.attempts = 9
# raises dataclasses.FrozenInstanceError
