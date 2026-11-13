"""Zero to AI Engineer · LLM Fundamentals · Part 13 of 18
Slide: One Wrong Word Breaks the Task
Run: python 01_one_wrong_word_breaks_the_task.py
"""
# Needs: pip install jiwer
# (not run while building this repo, because the package was not installed there)
import jiwer

ref = "reset the password for account 48213"
hyp = "reset the password for account 48230"
# about 0.17, one word in six wrong
print(jiwer.wer(ref, hyp))
# The wrong word is the account number,
# so the task fails.
