"""Zero to AI Engineer · RAG and Vector Search · Part 21 of 26
Follow-along lab: Simulate the MERGE trap
Run: python 03_lab_simulate_the_merge_trap.py
"""
CHK = ("Service", "checkout")
PAY = ("Team", "payments")
nodes, rels = [CHK], set()
def merge_path(a, b):
    if (a, b) not in rels:
        nodes.extend([a, b])
        rels.add((a, b))
merge_path(CHK, PAY)
print("whole path:", nodes.count(CHK))
merge_path(CHK, PAY)
print("rerun:", nodes.count(CHK))
# fix: merge each node on its key
good = list(dict.fromkeys([CHK, CHK, PAY]))
print("nodes first:", good.count(CHK))
