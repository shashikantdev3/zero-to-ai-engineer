"""Zero to AI Engineer · Python · Part 19 of 25
Follow-along lab: Prove lazy formatting yourself
Run: python 07_lab_prove_lazy_formatting_yourself.py
"""
import logging
calls = 0
class Chunk:
    def __str__(self):
        global calls
        calls += 1
        return "chunk"
log = logging.getLogger("app.retriever")
log.setLevel(logging.INFO)
log.debug("got %s", Chunk())
print("percent-s formatted:", calls)
log.debug(f"got {Chunk()}")
print("f-string formatted:", calls)
print("logger name:", log.name)
