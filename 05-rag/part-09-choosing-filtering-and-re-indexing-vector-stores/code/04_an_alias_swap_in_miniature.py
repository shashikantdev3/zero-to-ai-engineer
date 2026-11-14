"""Zero to AI Engineer · RAG and Vector Search · Part 9 of 26
Slide: An alias swap in miniature
Run: python 04_an_alias_swap_in_miniature.py
"""
# queries name the alias, never the index
aliases = {"runbooks": "runbooks_v1"}
built = {"runbooks_v1", "runbooks_v2"}
# golden set and recall passed on v2
v2_ok = True
if v2_ok and "runbooks_v2" in built:
    # one atomic step: replace the mapping
    aliases = {"runbooks": "runbooks_v2"}
print("serving:", aliases["runbooks"])
# rollback is one more swap
aliases = {"runbooks": "runbooks_v1"}
print("serving:", aliases["runbooks"])
