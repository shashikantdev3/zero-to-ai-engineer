"""Zero to AI Engineer · RAG and Vector Search · Part 19 of 26
Slide: A Chunk Record for a Diagram
Run: python 01_a_chunk_record_for_a_diagram.py
"""
# One chunk record for a diagram
chunk = {
    "type": "image_caption",
    "text": "Diagram: login flow via gateway",
    "image_uri": "docs/manual/fig3.png",
    "page": 12,
}
# the text is what search sees
print(chunk["text"])
# the pointer is what the citation shows
print(chunk["image_uri"], chunk["page"])
