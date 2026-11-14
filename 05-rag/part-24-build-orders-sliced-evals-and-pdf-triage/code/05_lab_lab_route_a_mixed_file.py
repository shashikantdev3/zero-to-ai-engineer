"""Zero to AI Engineer · RAG and Vector Search · Part 24 of 26
Follow-along lab: Lab: Route a Mixed File
Run: python 05_lab_lab_route_a_mixed_file.py
"""
pages = [
    {"n": 1, "text": "Annual report " * 10},
    {"n": 2, "text": "Results summary " * 5},
    {"n": 3, "text": "", "ocr_conf": 0.95},
    {"n": 4, "text": "", "ocr_conf": 0.62},
]
for p in pages:
    if len(p["text"].strip()) >= 50:
        print(f"page {p['n']}: text layer")
    elif p["ocr_conf"] >= 0.8:
        print(f"page {p['n']}: OCR, index")
    else:
        print(f"page {p['n']}: OCR, review")
