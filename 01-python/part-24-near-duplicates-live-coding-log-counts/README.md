# Python · Part 24 of 25: Near-Duplicates, Live Coding, Log Counts

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. MinHash for near-duplicate detection
2. Talking while coding (the meta-skill)
3. Parse a file and count occurrences
4. Question drill: file parsing task

## Key takeaways

- Signatures estimate Jaccard; bands pick candidates
- Clarify, approach, narrate, then verify
- Stream lines, count with Counter, merge shards
- Distinct keys decide memory; regex only extracts

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_shingles_in_code.py` | Shingles in code | yes |
| `code/02_minimum_hashes_in_code.py` | Minimum hashes in code | yes |
| `code/03_estimating_jaccard.py` | Estimating Jaccard | yes |
| `code/04_counting_emails_in_code.py` | Counting emails in code | yes |
| `code/05_merging_the_shards.py` | Merging the shards | yes |
| `code/06_lab_lab_count_across_shards.py` | Lab: count across shards | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/06_lab_lab_count_across_shards.py` prints:

```text
['bo@y.io']
[('ann@x.io', 2)]
distinct: 2
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A teammate says embed everything and drop pairs above 0.9 five cosine. What is the main problem?**

- A. Costly, and similar meaning is not duplicate
- B. Cosine cannot compare two documents
- C. Embeddings ignore the words entirely

<details><summary>Answer</summary>

**A. Costly, and similar meaning is not duplicate**. Duplicate means shared text, not shared meaning

</details>

**2. You code silently for twenty minutes, then say done. What is the real problem?**

- A. Twenty minutes is far too slow
- B. You needed more code comments
- C. You never showed that it works

<details><summary>Answer</summary>

**C. You never showed that it works**. Trace an example and list edge cases unasked

</details>

**3. Your solution reads the whole file and splits on newlines, and the file is forty gigabytes. What now?**

- A. Stream it with the file iterator
- B. Read it in one bigger chunk
- C. Split it with splitlines instead

<details><summary>Answer</summary>

**A. Stream it with the file iterator**. Iterate the file object; never read it whole

</details>

**4. An interviewer asks whether your email regex validates addresses. What is the honest answer?**

- A. Yes, as long as there is a dot
- B. No, it extracts likely addresses
- C. Yes, it follows the email standard

<details><summary>Answer</summary>

**B. No, it extracts likely addresses**. Extraction is the requirement, not validation

</details>

## Say it in the interview

**Say it: MinHash**

- Exact hashing misses near-duplicates
- Signatures estimate Jaccard; bands pick candidates
- Handle empty docs; never use built-in hash

**Say it: talking while coding**

- Confirm inputs and error behaviour first
- Naive, its problem, then the improved version
- Empty, one, boundary, failure path

**Say it: file counting**

- Stream, regex, lowercase, Counter
- Distinct keys decide memory, not file size
- Count per shard, merge: map-reduce

## Homework

- [ ] Run the MinHash demo; edit the footer
- [ ] Compute the threshold for 16 bands, 8 rows
- [ ] Write the email counter for a local log
- [ ] Practise five clarifying questions for retry
