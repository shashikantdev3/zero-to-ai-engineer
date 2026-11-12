"""Zero to AI Engineer · Python · Part 2 of 25
Slide: Ranking with a Tuple Key
Run: python 01_ranking_with_a_tuple_key.py
"""
results = [("d2", 0.8), ("d1", 0.8),
           ("d3", 0.9)]
ranked = sorted(results,
                key=lambda r: (-r[1], r[0]))
# ranked: d3, then d1, then d2
for rank, (doc, score) in enumerate(
        ranked, start=1):
    print(rank, doc, score)
