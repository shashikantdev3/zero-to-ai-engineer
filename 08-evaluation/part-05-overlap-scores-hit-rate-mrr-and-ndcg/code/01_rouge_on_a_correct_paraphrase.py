"""Zero to AI Engineer · Evaluation · Part 5 of 11
Slide: ROUGE on a correct paraphrase
Run: python 01_rouge_on_a_correct_paraphrase.py
"""
# Needs: pip install rouge_score
# (not run while building this repo, because the package was not installed there)
# pip install rouge-score
from rouge_score import rouge_scorer
s = rouge_scorer.RougeScorer(
    ["rougeL"], use_stemmer=True)
ref = "Carry forward up to 5 days."
out = "You may carry over five days."
score = s.score(ref, out)["rougeL"]
# low score for a correct paraphrase
print(score.fmeasure)
