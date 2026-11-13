# Python · Part 20 of 25: Lockfiles, Retries and Full Jitter

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Namespace packages, and why requirements.txt is not reproducible
2. Question drill: testing and tooling
3. Retry with capped exponential backoff
4. Full jitter

## Key takeaways

- No init file: namespace package. Commit a lockfile.
- Assert the call; evaluate quality separately
- Classify, cap, clamp, bound every attempt
- Randomise the whole delay to break the herd

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_parsing_retry_after_both_ways.py` | Parsing Retry-After both ways | yes |
| `code/02_each_attempt_inside_the_time_left.py` | Each attempt inside the time left | yes |
| `code/03_computing_the_next_delay.py` | Computing the next delay | yes |
| `code/04_the_retry_loop_itself.py` | The retry loop itself | yes |
| `code/05_full_jitter_in_one_line.py` | Full jitter in one line | yes |
| `code/06_lab_lab_plain_backoff_versus_jitter.py` | Lab: plain backoff versus jitter | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/06_lab_lab_plain_backoff_versus_jitter.py` prints:

```text
attempt 0 waits 0.5
attempt 3 waits 4.0
attempt 9 waits 20.0
no jitter: [2.0, 2.0, 2.0, 2.0]
full jitter: [0.6, 0.3, 1.3, 0.1]
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A teammate says pip freeze output is a clean, reproducible dependency spec. What is wrong?**

- A. It mixes direct, transitive and leftover packages
- B. It only works inside containers
- C. It does not pin any versions

<details><summary>Answer</summary>

**A. It mixes direct, transitive and leftover packages**. Pinned is not the same as clean

</details>

**2. In a unit test for code that calls an LLM, what should you assert?**

- A. The exact text of the reply
- B. That the reply reads well
- C. The call: prompt, parameters and tools

<details><summary>Answer</summary>

**C. The call: prompt, parameters and tools**. Unit test the call; evaluate quality separately

</details>

**3. Your retry wrapper catches every exception. What happens with a four oh one error?**

- A. It gives up too early
- B. It retries an error that cannot succeed
- C. Nothing, four oh ones are transient

<details><summary>Answer</summary>

**B. It retries an error that cannot succeed**. Classify first; retry only transient errors

</details>

**4. A server sends a Retry-After of thirty six hundred seconds. What should your client do?**

- A. Honour it, clamped, under a deadline
- B. Wait the full hour as told
- C. Ignore every Retry-After header

<details><summary>Answer</summary>

**A. Honour it, clamped, under a deadline**. Honour Retry-After, clamp it, enforce a deadline

</details>

**5. You check the deadline before each sleep. Is your total time now bounded?**

- A. Yes, every sleep is capped
- B. No, one attempt can hang for minutes
- C. Yes, attempts are limited to five

<details><summary>Answer</summary>

**B. No, one attempt can hang for minutes**. Bound each attempt with the time left

</details>

**6. Does plus or minus ten percent jitter break up a herd of a thousand clients?**

- A. Yes, any randomness is enough
- B. It makes no difference at all
- C. Only slightly, they stay clustered

<details><summary>Answer</summary>

**C. Only slightly, they stay clustered**. Small jitter keeps the herd; full jitter spreads it

</details>

## Say it in the interview

**Say it: packages and lockfiles**

- Missing init file: usually an accident in apps
- Bare names drift; freeze mixes intent and junk
- Ranges in pyproject, commit the lockfile

**Say it: retry with backoff**

- Classify first; fixed sleeps keep servers down
- Capped, jittered, clamped, inside the deadline
- Idempotency keys; retry in one layer

**Say it: full jitter**

- Plain backoff creates synchronised spikes
- One line, on by default

## Homework

- [ ] Check one project for missing init files
- [ ] Mark direct dependencies in a freeze output
- [ ] Write retry; test with a twice-failing fake
- [ ] Print full jitter delays and compare runs
