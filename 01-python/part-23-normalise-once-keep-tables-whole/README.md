# Python · Part 23 of 25: Normalise Once, Keep Tables Whole

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Normalise once
2. Tables whole

## Key takeaways

- One normalise function at ingest and query
- Never cut a table mid-row

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_normalise_and_normalise_code.py` | normalise and normalise_code | yes |
| `code/02_lab_watch_a_lookalike_hyphen_match.py` | Watch a lookalike hyphen match | yes |
| `code/03_chunk_route_blocks_by_type.py` | chunk: route blocks by type | yes |
| `code/04_pack_a_running_length_count.py` | pack: a running length count | yes |
| `code/05_split_table_repeat_the_header.py` | split_table: repeat the header | yes |
| `code/06_split_para_sentences_then_hard.py` | split_para: sentences, then hard | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_watch_a_lookalike_hyphen_match.py` prints:

```text
lower: False
code: True
value: xr4410b
digit: True
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. You call lower on the query, so why does a product code with a non-ASCII hyphen still miss?**

- A. Lower breaks the digits in the code
- B. The index was never normalised the same way
- C. The search index needs a rebuild

<details><summary>Answer</summary>

**B. The index was never normalised the same way**. Normalise both sides with one function

</details>

**2. After N F K C and then casefold, is the text always fully normalised?**

- A. No, apply N F K C again
- B. Only when the text is ASCII
- C. Yes, casefold keeps the normal form

<details><summary>Answer</summary>

**A. No, apply N F K C again**. Casefold can undo NFKC, so normalise again

</details>

**3. Someone says a bigger chunk size stops tables being cut, so what about a two hundred row table?**

- A. Drop the header to save space
- B. Double the chunk size again
- C. Split by rows and repeat the header

<details><summary>Answer</summary>

**C. Split by rows and repeat the header**. Split big tables by rows, header in each

</details>

**4. Your chunker gets one ten thousand character paragraph, so what keeps each chunk under the limit?**

- A. Sentence split with a hard split fallback
- B. Emitting the paragraph whole
- C. Raising the limit for paragraphs

<details><summary>Answer</summary>

**A. Sentence split with a hard split fallback**. Sentences first, hard split last

</details>

## Say it in the interview

**Normalise once, in the interview**

- One function, called at ingest and query
- Normalised field to match, original to cite
- Drift fails silently. Test on real data.

**Tables whole, in the interview**

- Chunk on structure, not characters
- Tables whole. Big ones split by rows.
- Linear, with metadata for citations

## Homework

- [ ] Write normalise from memory
- [ ] Test full-width digits and odd hyphens
- [ ] Check every table piece has the header
- [ ] Test a giant paragraph and empty input
