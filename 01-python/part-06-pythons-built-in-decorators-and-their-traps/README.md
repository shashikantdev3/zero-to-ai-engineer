# Python · Part 6 of 25: Python's Built-in Decorators and Their Traps

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Built-in decorators: property, staticmethod, classmethod, lru_cache, cached_property
2. Where stacking order bites: routes, auth and caches
3. Decorators run at import time
4. A decorator usable with and without arguments
5. Decorating methods: staticmethod and classmethod go outermost

## Key takeaways

- lru_cache leaks self; cached_property needs __dict__
- Route on top; checks inside caches
- Body at import, wrapper per call
- fn=None, keyword-only options, partial
- staticmethod and classmethod outermost

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_client_with_three_method_types.py` | A Client with Three Method Types | yes |
| `code/02_the_two_caching_decorators.py` | The Two Caching Decorators | yes |
| `code/03_a_router_and_a_login_check.py` | A Router and a Login Check | yes |
| `code/04_safe_order_versus_leaky_order.py` | Safe Order Versus Leaky Order | yes |
| `code/05_lab_reproduce_the_leaky_route.py` | Reproduce the Leaky Route | yes |
| `code/06_a_registry_decorator.py` | A Registry Decorator | yes |
| `code/07_the_retry_decorator.py` | The Retry Decorator | yes |
| `code/08_both_forms_in_use.py` | Both Forms in Use | yes |
| `code/09_logged_below_the_classmethod.py` | Logged Below the Classmethod | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_reproduce_the_leaky_route.py` prints:

```text
safe route: blocked
leaky route: secret
leaky name: blocked
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Why does memory keep growing when L R U cache decorates a method?**

- A. The cache keeps every self alive
- B. The cache copies the whole class
- C. Methods cannot be cached at all

<details><summary>Answer</summary>

**A. The cache keeps every self alive**. lru_cache on methods is not free: it holds self

</details>

**2. When the route decorator sits nearest the function, which function does the router store?**

- A. The login protected wrapper
- B. The bare, unprotected function
- C. Both, so the check still runs

<details><summary>Answer</summary>

**B. The bare, unprotected function**. Order decides what gets registered

</details>

**3. Why is the tool registry already full before any function is called?**

- A. The wrapper fills it on first call
- B. The decorator ran when def executed
- C. Python calls each function on import

<details><summary>Answer</summary>

**B. The decorator ran when def executed**. Decorators run at definition time, not call time

</details>

**4. With positional options, what does retry with just the number five do?**

- A. Treats five as the function, fails later
- B. Raises a clear error immediately
- C. Sets the retry count to five

<details><summary>Answer</summary>

**A. Treats five as the function, fails later**. Make options keyword-only

</details>

**5. If your own decorator sits above classmethod, what object does it receive?**

- A. The plain function, as usual
- B. The class itself
- C. A classmethod descriptor, not the function

<details><summary>Answer</summary>

**C. A classmethod descriptor, not the function**. staticmethod and classmethod go outermost

</details>

## Say it in the interview

**Say It in the Interview**

- property: computed attribute, callers unchanged
- classmethod builds; staticmethod just lives there
- lru_cache traps: unhashable args, leaked self

**Say It in the Interview**

- Built inside out, run outside in
- Route on top, login check below
- Checks inside the cache, or user in key

**Say It in the Interview**

- Body at import, wrapper per call
- Keep decorator bodies cheap

**Say It in the Interview**

- fn optional first; options keyword-only
- No fn: return partial. Got fn: wrap it.
- Without the star, @retry(5) passes 5 as fn

**Say It in the Interview**

- Ordinary methods: self is args[0]
- staticmethod and classmethod always outermost

## Homework

- [ ] Write a class with property and classmethod
- [ ] Swap the decorators in the route lab
- [ ] Watch a registry decorator fire on import
- [ ] Build retry that works bare and with options
