"""Zero to AI Engineer · Python · Part 22 of 25
Slide: Split successes from failures
Run: python 05_split_successes_from_failures.py
"""
def split(items, results):
    ok, failed = [], []
    for it, r in zip(items, results,
                     strict=True):
        if isinstance(r, BaseException):
            failed.append((it, r))
        else:
            ok.append((it, r))
    # retry failed with backoff, if safe
    return ok, failed
