import asyncio
import pytest
from worker_pool import WorkerPool, Task, DelayedTask


@pytest.mark.asyncio
async def test_successful_task_execution():
    # This test ensures that a simple task completes successfully without retries.
    async def simple_task():
        return "Success"

    task = Task(fn=simple_task)
    delayed_task = DelayedTask(task)
    await delayed_task.execute()
    result = await delayed_task.result()
    assert result == "Success"


@pytest.mark.asyncio
async def test_task_with_exception():
    # Tests that an exception is properly handled and re-raised if it's not retryable.
    async def faulty_task():
        raise ValueError("An error occurred")

    task = Task(fn=faulty_task, retryable_exceptions=(KeyError,))
    delayed_task = DelayedTask(task)
    with pytest.raises(ValueError):
        await delayed_task.execute()
        await delayed_task.result()


@pytest.mark.asyncio
async def test_task_with_retries():
    # Ensure that retries are attempted for retryable exceptions and succeed on retry.
    attempts = 0

    async def occasionally_faulty_task():
        nonlocal attempts
        attempts += 1
        if attempts < 2:
            raise TimeoutError("Timeout")
        return "Recovered"

    task = Task(fn=occasionally_faulty_task, retries=3, retryable_exceptions=(TimeoutError,))
    delayed_task = DelayedTask(task)
    await delayed_task.execute()
    result = await delayed_task.result()
    assert result == "Recovered"


@pytest.mark.asyncio
async def test_worker_pool_run():
    # Test running a single task through a WorkerPool
    async def simple_task():
        return 42

    workers = WorkerPool(size=1, empty_queue_timeout=1)
    task = Task(fn=simple_task)
    result = await workers.run(task)
    assert result == 42
    await workers.shutdown()


# @pytest.mark.asyncio
# async def test_worker_pool_shutdown():
#     # Test that tasks throw a CancelledError when the pool is shutdown abruptly.
#     async def long_running_task():
#         await asyncio.sleep(10)  # Simulate a long task
#         return "Done"

#     workers = WorkerPool(size=1)
#     task = Task(fn=long_running_task)
#     run_task = workers.run(task)

#     # Shutdown immediately, not waiting for tasks to finish
#     await workers.shutdown(wait_for_tasks=False)

#     with pytest.raises(asyncio.CancelledError):
#         await run_task


# @pytest.mark.asyncio
# async def test_semaphore_refill_rate_control():
#     # Ensure that the rate semaphore refills correctly according to the specified rate.
#     async def dummy_task():
#         return "OK"

#     rate = 1  # 1 task per second
#     workers = WorkerPool(size=None, rate=rate)
#     start_time = asyncio.get_event_loop().time()
#     task = Task(fn=dummy_task)
#     await workers.run(task)
#     await workers.run(task)  # Second run should wait for rate refill
#     elapsed_time = asyncio.get_event_loop().time() - start_time

#     assert elapsed_time >= 1  # At least one second should have passed due to rate limiting
