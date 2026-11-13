"""Zero to AI Engineer · Python · Part 21 of 25
Slide: Retry budget: may we retry?
Run: python 06_retry_budget_may_we_retry.py
"""
def can_retry() -> bool:
    now = time.monotonic()
    trim(now)
    # small floor for low traffic
    allowance = max(MIN_RETRIES,
                    RATIO * len(requests))
    if len(retries) < allowance:
        retries.append(now)
        return True
    return False
