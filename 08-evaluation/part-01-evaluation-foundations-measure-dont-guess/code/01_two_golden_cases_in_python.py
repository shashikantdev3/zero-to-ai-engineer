"""Zero to AI Engineer · Evaluation · Part 1 of 11
Slide: Two golden cases in Python
Run: python 01_two_golden_cases_in_python.py
"""
golden = [
    {"id": "leave-014", "category": "leave",
     "risk": "low", "must_abstain": False,
     "question": "How many casual leaves can"
                 " I carry forward?",
     "expected_doc_ids": ["HR-POL-LEAVE-v7"]},
    {"id": "pay-031", "category": "payroll",
     "risk": "high", "must_abstain": True,
     "question": "What was my bonus"
                 " last year?",
     "expected_doc_ids": []},
]
