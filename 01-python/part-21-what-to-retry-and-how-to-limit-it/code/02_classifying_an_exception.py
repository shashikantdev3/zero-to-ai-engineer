"""Zero to AI Engineer · Python · Part 21 of 25
Slide: Classifying an exception
Run: python 02_classifying_an_exception.py
"""
def exc_retryable(exc, safe):
    # httpx errors do not subclass the
    # built-in TimeoutError / ConnectionError
    if isinstance(exc, SAFE_T):
        return True
    builtin = (TimeoutError, ConnectionError)
    if isinstance(exc, UNKNOWN_T + builtin):
        return safe
    # any other transport error: unknown
    if isinstance(exc, httpx.TransportError):
        return safe
    return False
