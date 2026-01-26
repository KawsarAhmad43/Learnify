# Task: Rate Limiter

## Objective
Control.

## Setup
*   You are scraping a website. You must not send more than 5 requests per second.

## Task
1.  Use `asyncio.Semaphore(5)`.
2.  Create a worker function `scrape(url)` that:
    *   Acquires the semaphore: `async with sem:`
    *   Sleeps for 1 second (simulating work).
    *   Releases semaphore (automatic with context manager).
3.  **Task**: Launch 50 tasks. Observe that only 5 run at a time. The total time should be roughly 10 seconds.

## Question
What is `uvloop`?
*   Answer: A drop-in replacement for the default asyncio event loop, written in Cython (using libuv, same as Node.js). It makes Python asyncio 2-4x faster.
