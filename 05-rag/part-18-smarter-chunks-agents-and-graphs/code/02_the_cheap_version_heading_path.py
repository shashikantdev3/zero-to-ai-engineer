"""Zero to AI Engineer · RAG and Vector Search · Part 18 of 26
Slide: The cheap version: heading path
Run: python 02_the_cheap_version_heading_path.py
"""
from types import SimpleNamespace as NS
doc = NS(title="Leave Policy 2026")
chunk = NS(
    heading_path="India > Carry forward",
    text="Employees may carry forward"
         " up to ten days.",
)
text_to_index = (
    f"{doc.title} > {chunk.heading_path}\n"
    f"{chunk.text}"
)
print(text_to_index)
