"""Zero to AI Engineer · Evaluation · Part 7 of 11
Slide: DeepEval style: the setup
Run: python 06_deepeval_style_the_setup.py
"""
# Needs: pip install deepeval
# (not run while building this repo, because the package was not installed there)
# DeepEval style. Check the current docs.
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
    FaithfulnessMetric)
q = "Can unused leave carry forward?"
answer = "Yes, up to ten days."
chunks = ["Ten unused days carry forward."]
