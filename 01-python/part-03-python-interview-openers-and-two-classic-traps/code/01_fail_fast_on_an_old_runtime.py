"""Zero to AI Engineer · Python · Part 3 of 25
Slide: Fail fast on an old runtime
Run: python 01_fail_fast_on_an_old_runtime.py
"""
import sys

# TaskGroup and asyncio.timeout need 3.11
if sys.version_info < (3, 11):
    raise RuntimeError(
        "needs 3.11+ for TaskGroup"
        " and asyncio.timeout"
    )
