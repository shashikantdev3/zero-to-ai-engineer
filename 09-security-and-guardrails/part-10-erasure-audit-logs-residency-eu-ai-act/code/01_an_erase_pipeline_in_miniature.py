"""Zero to AI Engineer · Security and Guardrails · Part 10 of 11
Slide: An Erase Pipeline in Miniature
Run: python 01_an_erase_pipeline_in_miniature.py
"""
chunks = [{"id": "c1", "src": "doc7"},
          {"id": "c2", "src": "doc9"}]
cache = {"q1": "doc7", "q2": "doc9"}
traces = [{"req": "r1", "src": "doc7"}]
def erase(doc_id: str) -> None:
    for store in (chunks, traces):
        store[:] = [r for r in store
                    if r["src"] != doc_id]
    for k in [k for k, v in cache.items()
              if v == doc_id]:
        del cache[k]
erase("doc7")
