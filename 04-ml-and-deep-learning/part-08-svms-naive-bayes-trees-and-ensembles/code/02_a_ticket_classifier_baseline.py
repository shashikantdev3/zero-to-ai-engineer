"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 8 of 28
Slide: A ticket classifier baseline
Run: python 02_a_ticket_classifier_baseline.py
"""
# Needs: pip install scikit-learn
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import (
    CountVectorizer)
from sklearn.naive_bayes import MultinomialNB
texts = ["refund my order", "app crashes",
         "charged twice", "login error"]
labels = ["billing", "bug", "billing", "bug"]
nb = make_pipeline(CountVectorizer(),
                   MultinomialNB())
nb.fit(texts, labels)
print(nb.predict(["refund please"]))
