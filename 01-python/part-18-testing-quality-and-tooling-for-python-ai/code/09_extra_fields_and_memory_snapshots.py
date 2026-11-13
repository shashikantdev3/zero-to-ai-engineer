"""Zero to AI Engineer · Python · Part 18 of 25
Slide: Extra fields and memory snapshots
Run: python 09_extra_fields_and_memory_snapshots.py
"""
# --- repeated from 08_a_formatter_that_shows_the_id.py so this file runs on its own ---
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

# --- this slide ---
import logging, tracemalloc
log = logging.getLogger("svc")
log.addHandler(handler)
log.setLevel(logging.INFO)
# cid is printed, hits is not
log.info("retrieval done",
         extra={"cid": "abc123", "hits": 5})
tracemalloc.start()
# ... run workload ...
snap = tracemalloc.take_snapshot()
for stat in snap.statistics("lineno")[:5]:
    print(stat)
