# RAG and Vector Search · Part 20 of 26: RAPTOR, NL2SQL and When Graphs Pay Off

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. RAPTOR and hierarchical summarisation
2. NL2SQL and the semantic layer
3. Would a graph help? The unbounded-depth test
4. LazyGraphRAG and GraphRAG cost

## Key takeaways

- Summary tree answers whole-document questions
- Semantic layer, read-only role, compare result sets
- Use graphs for unknown-depth questions
- Baseline first; trial LazyGraphRAG small

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_validator_part_one_allowlists.py` | Validator part one: allowlists | after `pip install sqlglot` |
| `code/02_validator_part_two_one_select.py` | Validator part two: one SELECT | yes |
| `code/03_validator_part_three_tables_and_limit.py` | Validator part three: tables and limit | yes |
| `code/04_lab_same_rows_different_sql.py` | Same rows, different SQL | yes |
| `code/05_any_depth_in_plain_postgres.py` | Any depth in plain Postgres | yes |
| `code/06_the_recursive_step_and_cycle_guard.py` | The recursive step and cycle guard | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_same_rows_different_sql.py` prints:

```text
same text: False
reference rows: [(10,)]
generated rows: [(10,)]
same rows: True
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. For a 200-page report, what answers 'what is this report about'?**

- A. Summary nodes built from clustered chunks
- B. Retrieving more chunks per question
- C. Bigger chunks so the theme fits

<details><summary>Answer</summary>

**A. Summary nodes built from clustered chunks**. No chunk holds the theme. You need summaries.

</details>

**2. How should you score generated SQL against a reference query?**

- A. Count shared keywords in both queries
- B. Match the SQL text to the reference
- C. Run both and compare result sets

<details><summary>Answer</summary>

**C. Run both and compare result sets**. Compare result sets, not SQL strings

</details>

**3. The parser misses a clever bypass. What still protects the data?**

- A. The system prompt telling the model
- B. The read-only role and row-level security
- C. Nothing, the parser was the security

<details><summary>Answer</summary>

**B. The read-only role and row-level security**. The database enforces; the parser only helps

</details>

**4. Our data is relational. When does that justify a graph database?**

- A. Only if questions need unknown hop counts
- B. Whenever tables have foreign keys
- C. Always, relational data means use a graph

<details><summary>Answer</summary>

**A. Only if questions need unknown hop counts**. No unbounded-depth question, no graph

</details>

**5. Someone says GraphRAG beats vector RAG. What is the best reply?**

- A. Agreed, graphs always win
- B. It depends on domain, and costs far more
- C. No, graphs never improve retrieval

<details><summary>Answer</summary>

**B. It depends on domain, and costs far more**. Ask which domain, and at what token cost

</details>

## Say it in the interview

**RAPTOR in the interview**

- No single passage holds the document's theme
- Specific hits a leaf, broad hits a summary
- Add it only when the golden set shows failures

**NL2SQL in the interview**

- SQL is easy; meaning and safety are hard
- Perfect SQL, wrong question, plausible number
- Read-only role, views, limits, row-level security

**The graph test in the interview**

- The test is unknown depth, not relationships
- Recursive SQL covers much; dense nodes hurt graphs
- Rerankers are cheaper than entity resolution

**GraphRAG cost in the interview**

- Full GraphRAG's cost is the real problem
- Promising claim; I would test it
- Measure a reranked hybrid baseline first

## Homework

- [ ] Sketch a leaf and summary index
- [ ] Define three business terms precisely
- [ ] Rerun the lab with another equivalent query
- [ ] Find one unknown-depth question, or none
