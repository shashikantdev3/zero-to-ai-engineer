"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 9 of 28
Slide: SHAP values for five cases
Run: python 02_shap_values_for_five_cases.py
"""
# Needs: pip install pandas shap
# (not run while building this repo, because the package was not installed there)
import pandas as pd
import shap
# third-party; check docs for your version
X_trd = pd.DataFrame(X_tr)
X_vd = pd.DataFrame(X_val)
bg = X_trd.sample(100, random_state=42)
explainer = shap.Explainer(
    gb.predict_proba, bg)
# per-feature contributions for five cases
sv = explainer(X_vd.iloc[:5])
