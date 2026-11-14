"""Zero to AI Engineer · RAG and Vector Search · Part 20 of 26
Slide: Validator part two: one SELECT
Run: python 02_validator_part_two_one_select.py
"""
def parse_one(sql: str):
    s = sqlglot.parse(sql, read="postgres")
    if len(s) != 1 or s[0] is None:
        raise ValueError("one statement only")
    tree = s[0]
    if not isinstance(tree, exp.Select):
        raise ValueError("only SELECT allowed")
    if tree.args.get("into"):
        raise ValueError("no SELECT INTO")
    return tree
