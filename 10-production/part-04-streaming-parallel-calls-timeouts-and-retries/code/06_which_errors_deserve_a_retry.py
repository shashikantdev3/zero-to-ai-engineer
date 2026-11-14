"""Zero to AI Engineer · Production and LLMOps · Part 4 of 38
Slide: Which errors deserve a retry
Run: python 06_which_errors_deserve_a_retry.py
"""
import asyncio, random
BASE, CAP = 0.5, 20.0
# only errors that can succeed later
class Retryable(Exception):
    def __init__(self, retry_after=None):
        self.retry_after = retry_after
