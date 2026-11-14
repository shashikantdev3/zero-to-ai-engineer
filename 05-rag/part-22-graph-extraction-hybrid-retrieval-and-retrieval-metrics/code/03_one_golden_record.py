"""Zero to AI Engineer · RAG and Vector Search · Part 22 of 26
Slide: One golden record
Run: python 03_one_golden_record.py
"""
import json
record = {
    "id": "q-104",
    "question": "Can contractors take "
                "parental leave?",
    "relevant_chunk_ids":
        ["leave-policy-2026#s3-c2"],
    "source": "real",
    "tags": ["hr", "edge-case"],
}
print(json.dumps(record))
