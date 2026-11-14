# RAG and Vector Search · Part 24 of 26: Build Orders, Sliced Evals, and PDF Triage

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. The RAG take-home build order
2. Sliced retrieval evaluation
3. Question drill: Retrieval evaluation in practice
4. Ingestion triage
5. Per-page OCR

## Key takeaways

- Eval set first, then baseline, then requirements
- Metrics per segment, with case counts
- Test refusal, recall first, suspect the corpus
- Cheapest good parser, chosen per page
- OCR only what needs it; keep confidence

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_per_segment_report_in_pandas.py` | A Per-Segment Report in Pandas | yes |
| `code/02_spotting_broken_text.py` | Spotting Broken Text | yes |
| `code/03_is_the_page_mostly_image.py` | Is the Page Mostly Image? | after `pip install pymupdf` |
| `code/04_one_route_per_page.py` | One Route per Page | yes |
| `code/05_lab_lab_route_a_mixed_file.py` | Lab: Route a Mixed File | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_lab_route_a_mixed_file.py` prints:

```text
page 1: text layer
page 2: text layer
page 3: OCR, index
page 4: OCR, review
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Overall hit rate is 92%, but Legal says answers are wrong. What now?**

- A. Check Legal's hit rate and case count
- B. Nothing, the overall rate is high
- C. Upgrade to a bigger model

<details><summary>Answer</summary>

**A. Check Legal's hit rate and case count**. Slice the metric, and read the count too

</details>

**2. Your take-home scores 78% on 30 questions you wrote. What does that tell you?**

- A. Nothing, throw the eval set away
- B. The system is production ready
- C. Useful for comparing changes, not absolute

<details><summary>Answer</summary>

**C. Useful for comparing changes, not absolute**. Small self-written sets compare, they do not certify

</details>

**3. You have 10,000 messy PDFs. What is the best way to parse them?**

- A. Triage, send only hard pages to vision
- B. Send every page to a vision model
- C. Trust every text layer as it is

<details><summary>Answer</summary>

**A. Triage, send only hard pages to vision**. Route only hard pages; verify text layers

</details>

**4. A contract has 40 digital pages and 3 scanned ones. What should you OCR?**

- A. No pages, skip the scans
- B. Only the 3 scanned pages
- C. The whole file, to be consistent

<details><summary>Answer</summary>

**B. Only the 3 scanned pages**. Never trade exact text for OCR errors

</details>

## Say it in the interview

**Say It: Build Order**

- Eval set first, or every decision is taste
- Baseline, requirements, then measured upgrades
- A named flaw reads as judgement

**Say It: Sliced Evaluation**

- Slice by segment, show the sample size
- Content, vocabulary, permissions, in that order
- Gate the fixed slice in CI

**Say It: Ingestion Triage**

- Triage before you parse
- Verify text layers, do not trust them
- Vision models only for the hard pages

**Say It: Per-Page OCR**

- Files mix digital and scanned pages
- Decide OCR per page, keep confidence
- Flag low confidence, never index silently

## Homework

- [ ] Write ten golden questions, some unanswerable
- [ ] Tag segments, compute hit rate per slice
- [ ] Test looks_broken on clean and garbled text
- [ ] Change the lab threshold, watch routes change
