# RAG and Vector Search · Part 25 of 26: Turning Messy Documents into Trustworthy Chunks

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Reading order and layout analysis
2. Table structure extraction
3. Image captions
4. Chunk metadata
5. Confidence routing and Azure AI Document Intelligence

## Key takeaways

- Use position for order; strip repeated headers
- Keep tables whole, headers attached, totals checked
- Caption figures, mark generated, link the original
- Metadata enables filters, citations, permissions, debugging
- Thresholds plus rules; doubtful goes to review

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_checking_a_tables_total.py` | Checking a table's total | yes |
| `code/02_a_caption_record.py` | A caption record | yes |
| `code/03_a_chunk_with_its_metadata.py` | A chunk with its metadata | yes |
| `code/04_lab_route_extractions_by_confidence.py` | Route extractions by confidence | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_route_extractions_by_confidence.py` prints:

```text
accept
review: low amount
review: not in master
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A two-column page is read straight across. What does that do to retrieval?**

- A. Nothing, embeddings ignore word order
- B. Retrieval just runs a bit slower
- C. Chunks mix columns and mean nothing

<details><summary>Answer</summary>

**C. Chunks mix columns and mean nothing**. Wrong order makes meaningless chunks

</details>

**2. Row 40 of a table lands in a chunk without its header. What does it mean?**

- A. Nothing, the numbers lost their labels
- B. The model can infer the columns
- C. The same as with its header

<details><summary>Answer</summary>

**A. Nothing, the numbers lost their labels**. Keep headers with every table chunk

</details>

**3. A caption misreads a number in a chart. What protects the answer?**

- A. Cite the image, never caption alone
- B. Trust it, the model saw the chart
- C. Store the caption without the image

<details><summary>Answer</summary>

**A. Cite the image, never caption alone**. Captions are evidence, not ground truth

</details>

**4. You stored only text and a vector. How do you cite a page or delete a document's chunks?**

- A. Search the vectors for the file name
- B. You cannot, you need metadata
- C. Ask the model which page it was

<details><summary>Answer</summary>

**B. You cannot, you need metadata**. No metadata: no citations, no clean deletes

</details>

**5. An extracted field has confidence 0.95. Is the value correct?**

- A. Yes, above 0.9 means correct
- B. Not necessarily; add rules and sampling
- C. Only if every field is above 0.9

<details><summary>Answer</summary>

**B. Not necessarily; add rules and sampling**. Confidence is a signal, not proof

</details>

## Say it in the interview

**Explaining layout analysis**

- Naive extraction mixes both columns
- Position gives order and structure
- Markdown headings in, repeated headers out

**Explaining table extraction**

- Flat reading turns tables into garbage
- Whole table, header row and caption
- Totals must add up, or review

**Explaining image captions**

- Text search cannot see diagrams
- Caption, index, link back to source
- Mark generated, skip logos

**Explaining chunk metadata**

- Every chunk carries its own label
- Precise citations, current versions
- Permissions enforced, re-ingest safe

**Explaining confidence routing**

- Low confidence goes to human review
- Field-level confidence and coordinates
- Switch if accuracy stays below the bar

## Homework

- [ ] Run the total check on your own table
- [ ] Write metadata for one real chunk
- [ ] Add a cross-field rule to the router
- [ ] Explain reading order in two sentences
