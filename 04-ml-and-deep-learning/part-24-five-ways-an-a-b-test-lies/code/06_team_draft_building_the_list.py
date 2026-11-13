"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 24 of 28
Slide: Team Draft: Building the List
Run: python 06_team_draft_building_the_list.py
"""
def team_draft(a, b, k, rng):
    out, owner, na, nb = [], {}, 0, 0
    while len(out) < k:
        tie = na == nb and rng.random() < 0.5
        pick_a = na < nb or tie
        doc, team = take(a, b, pick_a, owner)
        if doc is None:
            break
        owner[doc] = "A" if team else "B"
        out.append(doc)
        na, nb = na + team, nb + (not team)
    return out, owner
