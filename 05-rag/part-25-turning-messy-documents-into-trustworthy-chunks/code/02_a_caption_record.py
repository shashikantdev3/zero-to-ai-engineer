"""Zero to AI Engineer · RAG and Vector Search · Part 25 of 26
Slide: A caption record
Run: python 02_a_caption_record.py
"""
caption = {
    "type": "image_caption",
    "generated": True,
    "text": "...",
    "image_uri": "...",
    "page": 7,
}
print(caption["generated"], caption["page"])
