"""Zero to AI Engineer · Python · Part 19 of 25
Slide: Lazy formatting and log.exception
Run: python 06_lazy_formatting_and_log_exception.py
"""
import logging

log = logging.getLogger(__name__)

def retrieve(n: int, tenant: str) -> None:
    log.debug("retrieved %s chunks for %s",
              n, tenant)
    try:
        raise TimeoutError("search timed out")
    except TimeoutError:
        # includes the traceback
        log.exception("retrieval failed")
