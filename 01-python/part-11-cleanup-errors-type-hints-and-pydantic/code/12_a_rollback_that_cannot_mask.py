"""Zero to AI Engineer · Python · Part 11 of 25
Slide: A Rollback That Cannot Mask
Run: python 12_a_rollback_that_cannot_mask.py
"""
import logging
log = logging.getLogger(__name__)

def rollback_quietly(conn):
    try:
        conn.rollback()
    except Exception:
        # never mask the original error
        log.exception("rollback failed")
