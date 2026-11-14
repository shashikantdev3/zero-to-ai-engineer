"""Zero to AI Engineer · RAG and Vector Search · Part 23 of 26
Slide: A golden case marked unanswerable
Run: python 01_a_golden_case_marked_unanswerable.py
"""
case = {
    "id": "q-201",
    "question": ("What is the leave policy"
                 " for interns in Brazil?"),
    "category": "unanswerable",
    "expected": "refusal",
    "relevant_chunk_ids": [],
}
print(case["category"], case["expected"])
