"""Zero to AI Engineer · RAG and Vector Search · Part 14 of 26
Slide: Put the heading path back in
Run: python 02_put_the_heading_path_back_in.py
"""
# Needs: pip install langchain_text_splitters
# (not run while building this repo, because the package was not installed there)
# --- repeated from 01_split_on_headings_first.py so this file runs on its own ---
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

# --- this slide ---
# chunk_size counts characters by default
rec = Rec(chunk_size=1000, chunk_overlap=150)
chunks = rec.split_documents(sections)
# prepend the heading path to embed it
for c in chunks:
    path = " > ".join(
        c.metadata[k] for _, k in HEADERS
        if k in c.metadata)
    text = c.page_content
    c.page_content = f"{path}\n{text}"
print(chunks[0].page_content)
