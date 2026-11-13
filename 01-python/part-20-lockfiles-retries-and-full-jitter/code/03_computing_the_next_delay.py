"""Zero to AI Engineer · Python · Part 20 of 25
Slide: Computing the next delay
Run: python 03_computing_the_next_delay.py
"""
class RetryableError(Exception):
    retry_after: float | None = None
def next_delay(i, e, dl, base=0.5,
               cap=20.0, max_ra=60.0):
    top = min(cap, base * 2 ** i)
    d = random.uniform(0, top)
    if e.retry_after is not None:
        d = max(d, min(e.retry_after, max_ra))
    t = time.monotonic() + d
    if t > dl:
        raise DeadlineExceeded from e
    return d
