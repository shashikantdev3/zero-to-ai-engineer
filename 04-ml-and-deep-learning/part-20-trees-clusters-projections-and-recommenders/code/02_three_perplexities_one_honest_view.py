"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 20 of 28
Slide: Three perplexities, one honest view
Run: python 02_three_perplexities_one_honest_view.py
"""
# Needs: pip install scikit-learn
from sklearn.datasets import make_blobs
from sklearn.manifold import TSNE
X_s, _ = make_blobs(300, n_features=10,
                    random_state=0)
for perp in (5, 30, 100):
    tsne = TSNE(n_components=2,
                perplexity=perp,
                random_state=0)
    emb2d = tsne.fit_transform(X_s)
    # plot each; trust only structure
    # that survives across settings
