# AsyncIO and Concurrency

## 1. Concurrency vs Parallelism
*   **Concurrency**: Doing multiple things at once (Interleaving). Efficient for I/O bound tasks (Waiting for Network).
*   **Parallelism**: Doing multiple things simultaneously (Multi-core). Efficient for CPU bound tasks (Calculating digits of Pi).

## 2. The `async` and `await` keywords
*   **Coroutine**: A function defined with `async def`. It returns a coroutine object.
*   **Await**: `await func()` pauses the current coroutine, yields control back to the Event Loop, and waits for `func()` to finish.

## 3. The Event Loop
*   The orchestrator that runs tasks. `asyncio.run(main())`.
*   It is single-threaded. It switches between tasks when they `await`.

## 4. Tasks
*   `asyncio.create_task(coro)` schedules a coroutine to run soon. This allows you to run multiple coroutines "concurrently".
