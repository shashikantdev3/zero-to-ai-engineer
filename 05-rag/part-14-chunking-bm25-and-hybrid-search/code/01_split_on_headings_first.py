"""Zero to AI Engineer · RAG and Vector Search · Part 14 of 26
Slide: Split on headings first
Run: python 01_split_on_headings_first.py
"""
# Needs: pip install langchain_text_splitters
# (not run while building this repo, because the package was not installed there)
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter as Md,
    RecursiveCharacterTextSplitter as Rec,
)
md = ("# Leave\n## Parental\n"
      "Unused days carry forward.")
HEADERS = [("#", "h1"), ("##", "h2"),
           ("###", "h3")]
split = Md(headers_to_split_on=HEADERS)
# strip_headers=True: headings go to metadata
sections = split.split_text(md)
