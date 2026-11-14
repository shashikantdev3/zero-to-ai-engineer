"""Zero to AI Engineer · RAG and Vector Search · Part 20 of 26
Slide: Validator part one: allowlists
Run: python 01_validator_part_one_allowlists.py
"""
# Needs: pip install sqlglot
# (not run while building this repo, because the package was not installed there)
import sqlglot
from sqlglot import exp

# Defence in depth only. The read-only
# role and row-level security are the
# real enforcement.
# Run with: SET statement_timeout = '5s';
VIEWS = {("reporting", "v_leave_requests"),
         ("reporting", "v_headcount")}
FUNCS = {"COUNT", "SUM", "AVG", "MIN", "MAX",
         "COALESCE", "CAST", "DATE_TRUNC"}
