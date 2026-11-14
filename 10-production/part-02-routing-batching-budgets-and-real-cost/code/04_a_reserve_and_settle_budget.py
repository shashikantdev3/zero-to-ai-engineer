"""Zero to AI Engineer · Production and LLMOps · Part 2 of 38
Slide: A reserve and settle budget
Run: python 04_a_reserve_and_settle_budget.py
"""
class Budget:
    def __init__(self, limit_usd):
        self.limit = limit_usd
        self.spent = self.reserved = 0.0
    def reserve(self, worst):
        used = self.spent + self.reserved
        if used + worst > self.limit:
            raise RuntimeError("over budget")
        self.reserved += worst
    def settle(self, worst, actual):
        self.reserved -= worst
        self.spent += actual
