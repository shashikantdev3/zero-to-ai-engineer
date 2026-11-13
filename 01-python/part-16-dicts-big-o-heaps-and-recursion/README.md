# Python · Part 16 of 25: Dicts, Big O, Heaps and Recursion

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Dict and set internals and hashing
2. Complexity of built-in operations
3. collections, heapq and bisect
4. Recursion, depth limit, memoisation and flattening a nested dictionary
5. Why list append is amortised O(1), and how the compact dict stays ordered

## Key takeaways

- Hash tables: O(1) average; persist with hashlib.
- List front is O(n); queues use deque.
- heapq is min-heap; top-k is n log k.
- Deep or untrusted input: explicit stack.
- Amortised append; dict ordered, set not.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_stable_key_with_hashlib.py` | A stable key with hashlib | yes |
| `code/02_counter_defaultdict_and_deque.py` | Counter, defaultdict and deque | yes |
| `code/03_top_k_with_heapq_buckets_with_bisect.py` | Top k with heapq, buckets with bisect | yes |
| `code/04_lab_containers_in_five_prints.py` | Containers in five prints | yes |
| `code/05_flatten_the_recursive_way.py` | Flatten, the recursive way | yes |
| `code/06_flatten_with_an_explicit_stack.py` | Flatten with an explicit stack | yes |
| `code/07_watching_a_list_grow.py` | Watching a list grow | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_containers_in_five_prints.py` prints:

```text
[('429', 2)]
[80, 95, 300]
1
[0.9, 0.5]
1
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. You use Python's built-in hash of the text as a Redis cache key. Why does every restart miss the cache?**

- A. String hashes are randomised per process
- B. Dicts lose insertion order on restart
- C. Redis clears all keys on restart

<details><summary>Answer</summary>

**A. String hashes are randomised per process**. Durable keys need hashlib, never built-in hash.

</details>

**2. Your breadth first search uses list pop at index zero as its queue. What is its worst case now?**

- A. Still linear in nodes plus edges
- B. Order of V squared
- C. Order of V log V

<details><summary>Answer</summary>

**B. Order of V squared**. BFS queue: deque.popleft, never list.pop(0).

</details>

**3. Someone says heap Q gives a max heap. Which item sits at index zero?**

- A. The most recently pushed item
- B. The largest item
- C. The smallest item

<details><summary>Answer</summary>

**C. The smallest item**. heapq is a min-heap; negate keys for max.

</details>

**4. An interviewer asks you to flatten a nested dictionary. Which answer holds up best?**

- A. Raise the recursion limit, then recurse
- B. Write it, and discuss separator collisions
- C. Just call pandas json normalize

<details><summary>Answer</summary>

**B. Write it, and discuss separator collisions**. Write it yourself; watch keys containing the separator.

</details>

**5. Someone claims every single list append is constant time. Is that right?**

- A. No, a resizing append is linear
- B. No, every append is linear
- C. Yes, every append is constant

<details><summary>Answer</summary>

**A. No, a resizing append is linear**. Amortised O(1); the resizing append is O(n).

</details>

## Say it in the interview

**Say it in the interview**

- Hash the key, jump, probe on collision.
- Average O(1), worst O(n), stable keys.
- Durable IDs: SHA-256 of normalised text.

**Say it in the interview**

- List front is linear: everything shifts.
- Dedup with a set, queue with a deque.
- State complexity first, then check every line.

**Say it in the interview**

- Counter for frequencies, defaultdict for grouping.
- Top-k: heap of size k, n log k.
- bisect is log n; insort is linear.

**Say it in the interview**

- Recurse into non-empty dicts, write leaves: O(n).
- json_normalize hides logic and adds weight.
- Untrusted depth: explicit stack, no tail calls.

**Say it in the interview**

- Over-allocate, grow proportionally, copy rarely.
- One slow append matters for strict latency.
- Dense entries plus sparse indices keep order.

## Homework

- [ ] Replace stored hash() keys with SHA-256
- [ ] Swap a list.pop(0) queue for deque
- [ ] Write flatten from memory, both versions
- [ ] Run the growth script, note the jumps
