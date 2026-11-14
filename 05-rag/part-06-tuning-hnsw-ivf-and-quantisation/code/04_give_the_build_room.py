"""Zero to AI Engineer · RAG and Vector Search · Part 6 of 26
Slide: Give the build room
Run: python 04_give_the_build_room.py
"""
# Illustrative: size memory to the machine
setup = [
    "SET maintenance_work_mem = '8GB';",
    "SET max_parallel_maintenance_workers"
    " = 7;",
    "CREATE INDEX ON chunks USING hnsw"
    " (embedding vector_cosine_ops);",
]
for stmt in setup:
    print(stmt)
