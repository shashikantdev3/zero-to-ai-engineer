"""Zero to AI Engineer · Python · Part 20 of 25
Slide: Parsing Retry-After both ways
Run: python 01_parsing_retry_after_both_ways.py
"""
from datetime import datetime, UTC
from email.utils import parsedate_to_datetime

def parse_ra(v: str | None) -> float | None:
    if v is None:
        return None
    if v.strip().isdigit():
        return float(v)
    when = parsedate_to_datetime(v)
    now = datetime.now(UTC)
    secs = (when - now).total_seconds()
    return max(0.0, secs)
