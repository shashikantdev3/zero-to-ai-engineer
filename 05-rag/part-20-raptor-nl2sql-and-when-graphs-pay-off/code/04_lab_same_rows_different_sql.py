"""Zero to AI Engineer · RAG and Vector Search · Part 20 of 26
Follow-along lab: Same rows, different SQL
Run: python 04_lab_same_rows_different_sql.py
"""
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE leave(id, days)")
rows = [(1, 3), (2, 5), (3, 2)]
ins = "INSERT INTO leave VALUES (?, ?)"
db.executemany(ins, rows)
gold = "SELECT SUM(days) FROM leave"
pred = "SELECT SUM(l.days) FROM leave AS l"
a = db.execute(gold).fetchall()
b = db.execute(pred).fetchall()
print("same text:", gold == pred)
print("reference rows:", a)
print("generated rows:", b)
print("same rows:", a == b)
