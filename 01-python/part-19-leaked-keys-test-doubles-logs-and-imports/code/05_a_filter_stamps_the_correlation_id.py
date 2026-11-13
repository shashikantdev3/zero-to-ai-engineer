"""Zero to AI Engineer · Python · Part 19 of 25
Slide: A filter stamps the correlation id
Run: python 05_a_filter_stamps_the_correlation_id.py
"""
import contextvars, logging
correlation_id = contextvars.ContextVar(
    "correlation_id", default="-")

class CorrelationFilter(logging.Filter):
    def filter(self, record) -> bool:
        cid = correlation_id.get()
        record.correlation_id = cid
        return True
# in a library package's __init__.py:
logging.getLogger("mylib").addHandler(
    logging.NullHandler())
