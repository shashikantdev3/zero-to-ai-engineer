"""Zero to AI Engineer · RAG and Vector Search · Part 24 of 26
Slide: One Route per Page
Run: python 04_one_route_per_page.py
"""
def route(page):
    text = page.get_text().strip()
    if len(text) < 50:
        return "ocr"
    bad = looks_broken(text)
    if mostly_image(page) or bad:
        return "ocr_or_layout"
    return "text_layer"

def triage(path):
    with pymupdf.open(path) as doc:
        return [route(p) for p in doc]
