"""Zero to AI Engineer · Python · Part 18 of 25
Slide: parametrize a retry rule
Run: python 01_parametrize_a_retry_rule.py
"""
# Needs: pip install pytest
import pytest

RETRYABLE = {429, 500, 502, 503, 504}
def should_retry(status: int) -> bool:
    return status in RETRYABLE

CASES = [(429, True), (503, True),
         (400, False), (401, False)]

@pytest.mark.parametrize("status,exp", CASES)
def test_should_retry(status, exp):
    assert should_retry(status) is exp
