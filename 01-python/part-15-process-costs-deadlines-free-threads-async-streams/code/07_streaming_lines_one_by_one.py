"""Zero to AI Engineer · Python · Part 15 of 25
Slide: Streaming Lines One by One
Run: python 07_streaming_lines_one_by_one.py
"""
async def stream_lines(client, url):
    async with client.stream("GET", url) as r:
        async for line in r.aiter_lines():
            if line:
                yield line
