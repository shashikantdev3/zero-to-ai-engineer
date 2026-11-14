"""Zero to AI Engineer · RAG and Vector Search · Part 24 of 26
Slide: Is the Page Mostly Image?
Run: python 03_is_the_page_mostly_image.py
"""
# Needs: pip install pymupdf
# (not run while building this repo, because the package was not installed there)
import pymupdf
# older code uses: import fitz

def mostly_image(page):
    area = page.rect.width * page.rect.height
    img = 0
    for im in page.get_images(full=True):
        for r in page.get_image_rects(im[0]):
            img += r.width * r.height
    return area > 0 and img / area > 0.8
