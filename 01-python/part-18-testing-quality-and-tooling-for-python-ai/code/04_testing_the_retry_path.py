"""Zero to AI Engineer · Python · Part 18 of 25
Slide: Testing the retry path
Run: python 04_testing_the_retry_path.py
"""
from unittest.mock import AsyncMock

def test_retries_then_succeeds():
    client = AsyncMock()
    client.complete.side_effect = [
        RateLimited(), " URGENT "]
    result = asyncio.run(
        classify(client, "server down"))
    assert result == "urgent"
    assert client.complete.await_count == 2
