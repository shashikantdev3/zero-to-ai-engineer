"""Zero to AI Engineer · LLM Fundamentals · Part 13 of 18
Slide: Search a Chart With Words
Run: python 02_search_a_chart_with_words.py
"""
# Needs: pip install pillow sentence_transformers
# (not run while building this repo, because the package was not installed there)
from PIL import Image
from sentence_transformers import (
    SentenceTransformer, util)

model = SentenceTransformer("clip-ViT-B-32")
img = Image.open("dashboard.png")
img_emb = model.encode(img)
txt_emb = model.encode(
    ["error rate spike on a line chart"])
print(util.cos_sim(img_emb, txt_emb))
