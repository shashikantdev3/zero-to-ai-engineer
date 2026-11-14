"""Zero to AI Engineer · RAG and Vector Search · Part 20 of 26
Slide: Validator part three: tables and limit
Run: python 03_validator_part_three_tables_and_limit.py
"""
def check(sql: str) -> str:
    tree = parse_one(sql)
    found = tree.find_all(exp.Table)
    tables = {(t.db, t.name) for t in found}
    if not tables or not tables <= VIEWS:
        raise ValueError(f"tables: {tables}")
    for f in tree.find_all(exp.Func):
        anon = isinstance(f, exp.Anonymous)
        n = f.name if anon else f.sql_name()
        if n.upper() not in FUNCS:
            raise ValueError(f"function: {n}")
    return tree.limit(1000).sql("postgres")
