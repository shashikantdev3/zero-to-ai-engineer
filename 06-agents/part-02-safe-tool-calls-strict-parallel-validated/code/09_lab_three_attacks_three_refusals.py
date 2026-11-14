"""Zero to AI Engineer · Agents and Tools · Part 2 of 26
Follow-along lab: Three attacks, three refusals
Run: python 09_lab_three_attacks_three_refusals.py
"""
import sqlite3
from pathlib import Path
from urllib.parse import urlparse
BASE = Path("/srv/runbooks").resolve()
p = (BASE / "../../etc/passwd").resolve()
print("inside base:", p.is_relative_to(BASE))
ALLOWED = {"status.internal.example.com"}
u = urlparse("http://169.254.169.254/")
print("url allowed:", u.hostname in ALLOWED)
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE t AS SELECT 'u1' o")
q = "SELECT * FROM t WHERE o = ?"
rows = db.execute(q, ("u1' OR '1'='1",))
print("injection rows:", len(rows.fetchall()))
