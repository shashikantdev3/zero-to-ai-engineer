"""Zero to AI Engineer · Python · Part 18 of 25
Slide: A formatter that shows the ID
Run: python 08_a_formatter_that_shows_the_id.py
"""
import logging

class CorrelationDefault(logging.Filter):
    def filter(self, record) -> bool:
        if not hasattr(record, "cid"):
            record.cid = "-"
        return True

handler = logging.StreamHandler()
handler.addFilter(CorrelationDefault())
handler.setFormatter(logging.Formatter(
    "%(levelname)s cid=%(cid)s %(message)s"))
