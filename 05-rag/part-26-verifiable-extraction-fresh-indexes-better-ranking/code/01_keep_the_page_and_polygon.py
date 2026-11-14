"""Zero to AI Engineer · RAG and Vector Search · Part 26 of 26
Slide: Keep the page and polygon
Run: python 01_keep_the_page_and_polygon.py
"""
from types import SimpleNamespace as NS
# stand-in for a layout result
reg = NS(page_number=2, polygon=[1, 2, 4, 2])
para = NS(content="Total: 1,250 EUR",
          bounding_regions=[reg])
result = NS(paragraphs=[para])
for para in result.paragraphs:
    region = para.bounding_regions[0]
    chunk_meta = {"page": region.page_number,
                  "polygon": region.polygon,
                  "text": para.content}
# field confidence drives review routing
