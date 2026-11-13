"""Zero to AI Engineer · Python · Part 21 of 25
Slide: Sorting the errors
Run: python 01_sorting_the_errors.py
"""
# Needs: pip install httpx
import httpx
NOT_PROCESSED = {429, 503}
# may have committed upstream (408: cautious)
UNKNOWN = {408, 500, 502, 504}
# request never sent: safe even for writes
SAFE_T = (httpx.ConnectError,
          httpx.ConnectTimeout,
          httpx.PoolTimeout)
# request may have reached the server
UNKNOWN_T = (httpx.ReadTimeout,
             httpx.WriteTimeout,
             httpx.RemoteProtocolError)
