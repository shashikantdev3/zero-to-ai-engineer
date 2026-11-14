# RAG and Vector Search · Part 8 of 26: Vector Indexes at Scale and Over Time

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Disk-based indexes: DiskANN and SPANN
2. Deletes, tombstones and recall drift
3. The index is derived data
4. Reading vector benchmarks

## Key takeaways

- Quantise, disk index, then shard
- Tombstones drift recall; check it on schedule
- Back up sources; rebuild time is your RTO
- Compare at equal recall, on your data

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_pg_diskann_in_azure_postgresql.py` | pg_diskann in Azure PostgreSQL | yes |
| `code/02_a_scheduled_recall_check.py` | A scheduled recall check | yes |
| `code/03_running_the_check.py` | Running the check | yes |
| `code/04_timing_a_full_rebuild.py` | Timing a full rebuild | yes |
| `code/05_exact_baseline_and_recall.py` | Exact baseline and recall | yes |
| `code/06_compare_at_equal_recall.py` | Compare at equal recall | yes |
| `code/07_lab_equal_recall_changes_the_winner.py` | Equal recall changes the winner | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/07_lab_equal_recall_changes_the_winner.py` prints:

```text
unfair: 2.0 vs 1.5
A at 0.95: (64, 4.0)
B at 0.95: (128, 6.0)
winner: A
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your vectors no longer fit in RAM. What do you try first?**

- A. Quantise the vectors
- B. Shard across more machines
- C. Switch to exact brute-force search

<details><summary>Answer</summary>

**A. Quantise the vectors**. Quantise, then a disk index, then shard

</details>

**2. Recall was 0.94 at launch, months ago. Is the index still fine?**

- A. Yes, because no alert has fired
- B. Unknown until you measure again
- C. Yes, recall does not change

<details><summary>Answer</summary>

**B. Unknown until you measure again**. Recall belongs on a schedule

</details>

**3. You snapshot the index every night. Is recovery covered?**

- A. No, back up access lists and test
- B. Yes, the snapshot has everything
- C. Yes, if embeddings are stored too

<details><summary>Answer</summary>

**A. No, back up access lists and test**. Back up ACLs and test the restore

</details>

**4. A vendor table shows lower latency than your store. Should you switch?**

- A. Yes, lower latency always wins
- B. Yes, if the table is recent
- C. Only after equal-recall tests on your data

<details><summary>Answer</summary>

**C. Only after equal-recall tests on your data**. Compare at equal recall on your own corpus

</details>

## Say it in the interview

**Say it in the interview**

- Quantise first: int8 cuts vectors to a quarter
- Then a disk index: DiskANN or SPANN
- Shard last: it creates a distributed system

**Say it in the interview**

- Launch recall is history, not a monitor
- Tombstones make high-churn graphs degrade quietly
- Scheduled recall checks, alerts, periodic rebuilds

**Say it in the interview**

- The index is derived data
- Measured rebuild time is the real recovery time
- Migrations break on ids and ACLs

**Say it in the interview**

- Public tables differ in data, authors, recall
- Own data, exact baseline, p95 at equal recall@10

## Homework

- [ ] Write the quantise, disk, shard answer
- [ ] Make the recall check pass, then fail
- [ ] List what your backup must include
- [ ] Tweak the lab so B wins fairly
