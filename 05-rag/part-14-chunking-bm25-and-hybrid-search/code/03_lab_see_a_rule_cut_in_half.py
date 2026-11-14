"""Zero to AI Engineer · RAG and Vector Search · Part 14 of 26
Follow-along lab: See a rule cut in half
Run: python 03_lab_see_a_rule_cut_in_half.py
"""
text = ("Staff get ten leave days. "
        "Unused days carry forward.")
words = text.split()
def chunk(w, size, overlap):
    step = size - overlap
    return [" ".join(w[i:i + size])
            for i in range(0, len(w), step)]
for c in chunk(words, 6, 0):
    print(c)
print("---")
for c in chunk(words, 6, 2):
    print(c)
