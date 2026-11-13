"""Zero to AI Engineer · Python · Part 13 of 25
Slide: A process pool from asyncio
Run: python 01_a_process_pool_from_asyncio.py
"""
import asyncio
import concurrent.futures as cf
def cpu_heavy(text: str) -> int:
    return sum(ord(c) for c in text)
async def main(texts):
    loop = asyncio.get_running_loop()
    with cf.ProcessPoolExecutor() as pool:
        jobs = [loop.run_in_executor(pool,
                cpu_heavy, t) for t in texts]
        return await asyncio.gather(*jobs)
if __name__ == "__main__":
    print(asyncio.run(main(["a", "b"])))
