# LLM Fundamentals · Part 13 of 18: Voice Agents and Image-Text Embeddings

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Speech and audio models
2. Multimodal embeddings: contrastive image-text models
3. Speech in and out: ASR, TTS and voice agents

## Key takeaways

- Pipeline for audit, native for speed
- One space for meaning, not exact numbers
- Stream, guard the transcript, track p95

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_one_wrong_word_breaks_the_task.py` | One Wrong Word Breaks the Task | after `pip install jiwer` |
| `code/02_search_a_chart_with_words.py` | Search a Chart With Words | after `pip install pillow sentence_transformers` |
| `code/03_lab_error_rate_and_the_slow_tail.py` | Error Rate and the Slow Tail | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_error_rate_and_the_slow_tail.py` prints:

```text
WER: 0.17
Account number right: False
Average ms: 432
p95 ms: 1500
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Users say the voice agent cuts them off mid-sentence. What is the fix?**

- A. Tune the end-of-turn threshold on recordings
- B. Switch to a bigger chat model
- C. Lower the overall word error rate

<details><summary>Answer</summary>

**A. Tune the end-of-turn threshold on recordings**. Cut-offs mean an aggressive end-of-turn threshold

</details>

**2. Why did a CLIP search for 'revenue 4.2 million' miss the right chart?**

- A. The cosine threshold was set too low
- B. CLIP captures overall meaning, not fine text
- C. Charts cannot be embedded at all

<details><summary>Answer</summary>

**B. CLIP captures overall meaning, not fine text**. Exact values need OCR or a vision model

</details>

**3. Users say the voice agent feels slow. What should you measure?**

- A. Word error rate of the transcript
- B. Average end-to-end latency
- C. 95th percentile time to first audio

<details><summary>Answer</summary>

**C. 95th percentile time to first audio**. Users feel first audio and the slow tail

</details>

## Say it in the interview

**Speech Models**

- Pipeline when I need audit and guardrails
- Native when latency beats inspection
- Report entity accuracy separately

**Multimodal Search**

- CLIP for cheap search, VLMs for understanding
- Caption once at ingest, then index
- Scores are relative; tune on labelled pairs

**Voice Agents**

- Choose the design, then stream every stage
- p95 time to first audio, not the average
- Entity accuracy apart from word error rate

## Homework

- [ ] Rerun the lab with a second wrong word
- [ ] Score entities separately from word error rate
- [ ] Sketch a voice pipeline with its checkpoint
- [ ] Explain why CLIP cannot read chart numbers
