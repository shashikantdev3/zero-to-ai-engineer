"""Zero to AI Engineer · Python · Part 5 of 25
Slide: The async version
Run: python 05_the_async_version.py
"""
import functools, time
# timed() picks this when inspect says async
def timed_async(fn):
    @functools.wraps(fn)
    async def awrapper(*args, **kwargs):
        t = time.perf_counter()
        try:
            return await fn(*args, **kwargs)
        finally:
            dt = time.perf_counter() - t
            print(f"{fn.__name__}: {dt:.3f}s")
    return awrapper
