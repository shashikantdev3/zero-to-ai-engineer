"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 24 of 28
Slide: Team Draft: Taking a Pick
Run: python 05_team_draft_taking_a_pick.py
"""
import random

def take(a, b, pick_a, owner):
    # try the picking team, then the other
    for team in (pick_a, not pick_a):
        ranking = a if team else b
        for doc in ranking:
            if doc not in owner:
                return doc, team
    return None, pick_a
