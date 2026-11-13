"""Zero to AI Engineer · Python · Part 21 of 25
Slide: The final decision
Run: python 03_the_final_decision.py
"""
def is_retryable(status, exc, *,
                 idempotent, has_key=False):
    safe = idempotent or has_key
    if exc is not None:
        return exc_retryable(exc, safe)
    if status in NOT_PROCESSED:
        return True
    if status in UNKNOWN:
        # a retried 502 refund may double
        return safe
    return False
