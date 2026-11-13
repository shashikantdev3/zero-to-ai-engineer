"""Zero to AI Engineer · Python · Part 25 of 25
Slide: Cleanup with weakref.finalize
Run: python 04_cleanup_with_weakref_finalize.py
"""
import weakref
class TempResource:
    def __init__(self, path: str):
        self.path = path
        self._fin = weakref.finalize(
            self, print, f"cleanup {path}")
    def close(self) -> None:
        # explicit, idempotent cleanup
        self._fin()

r = TempResource("/tmp/x")
r.close()
