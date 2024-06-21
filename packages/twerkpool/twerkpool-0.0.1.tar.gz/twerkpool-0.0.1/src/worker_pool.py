"""
This module provides tools for managing asynchronous tasks with controlled concurrency and rate limits.
It includes a Task definition for scheduled execution and a WorkerPool to manage multiple tasks using asyncio.

Classes:
    Task: Defines a function to be executed asynchronously, with optional timeout and retry settings.
    WorkerPool: Manages a pool of tasks, enforcing concurrency and rate limits.
"""

__all__ = ["Task", "WorkerPool"]

import asyncio
from collections import deque
from contextlib import contextmanager
from math import ceil
import random
from typing import Any, Awaitable, Callable, Deque, List, NamedTuple


class Task(NamedTuple):
    fn: Callable[[], Awaitable[Any]]
    timeout: int | None = None
    retries: int = 0
    retryable_exceptions: List[type[Exception]] = [Exception]
    backoff: Callable[[int], float] = lambda attempts: 2**attempts + random.uniform(0, 1)


class DelayedTask:
    task: Task
    future: asyncio.Future

    def __init__(self, task: Task):
        self.task = task
        self.future = asyncio.Future()
        self.attempts = 0

    async def execute(self, callback: Callable[[], None]):
        while True:
            try:
                if self.task.timeout:
                    result = await asyncio.wait_for(self.task.fn(), self.task.timeout)
                else:
                    result = await self.task.fn()

                self.future.set_result(result)
                callback()
                break
            except Exception as e:
                if not any(isinstance(e, exc) for exc in self.task.retryable_exceptions):
                    self.future.set_exception(e)
                    break
                self.attempts += 1
                if self.attempts >= self.task.retries:
                    self.future.set_exception(e)
                    break
                await asyncio.sleep(self.task.backoff(self.attempts))

    async def result(self):
        return await self.future


class Semaphore:
    value: int | None
    semaphore: asyncio.Semaphore | None

    def __init__(self, value: int | None):
        self.value = value
        if value:
            self.semaphore = asyncio.Semaphore(value)

    async def acquire(self):
        if self.value:
            return await self.semaphore.acquire()

    def release(self):
        if self.value:
            return self.semaphore.release()

class WorkerPool:
    size: int | None
    rate: float | None
    count: int

    def __init__(self, size: int | None = None, rate: float | None = None):
        """
        Initializes a new WorkerPool class. Params size, rate or both must be provided.

        :param
            size: specifies the maximum number of concurrent workers that can be executing
                tasks. If None or not provided, no limit will be set.

            rate: specifies the maximum number of executions per second. If None or not
                provided, the rate is unbounded.

        Example usage:
            workers = WorkerPool(size=5, rate=10)
            # This creates a WorkerPool that allows up to 5 concurrent workers,
            # with a maximum rate of 10 executions per second.
        """

        if size and (size <= 0 or round(size) != size):
            raise ValueError("Size must be a positive integer or None.")
        if rate and rate <= 0:
            raise ValueError("Rate must be a positive float or None.")

        self.size = size
        self.rate = rate
        self.count = 0
        self._queue: Deque[DelayedTask] = deque()
        self._has_tasks = asyncio.Event()
        self._has_workers = asyncio.Event()
        self._has_workers.set()
        self._working = True

        self._semaphore = Semaphore(ceil(self.rate) if self.rate else None) # ceil: still need capcaity for partial (e.g. 0.5)
        self._wait = 1 / self.rate if self.rate else 0

        asyncio.create_task(self._release(), name=f'{self.__class__.__name__}.{self._release.__name__}')
        asyncio.create_task(self._work(), name=f'{self.__class__.__name__}.{self._work.__name__}')

    def _put_task(self, task: DelayedTask):
        self._queue.append(task)
        self._has_tasks.set()

    async def _get_task(self):
        await self._has_tasks.wait()
        # lock, take, check, release
        self._has_tasks.clear()
        task = self._queue.popleft()
        if len(self._queue) > 0:
            self._has_tasks.set()
        return task

    def _mark_done(self):
        self.count -= 1
        self._has_workers.set()

    async def _acquire_worker(self):
        await asyncio.gather(self._has_workers.wait(), self._semaphore.acquire())
        # lock, take, check, release
        self._has_workers.clear()
        self.count += 1
        if self.size is None or self.count < self.size:
            self._has_workers.set()

    async def _release(self):
        # only ever called once, at initialization
        while bool(self.rate) and self._working:
            await asyncio.gather(asyncio.sleep(self._wait), self._has_tasks.wait())
            self._semaphore.release()

    async def _work(self):
        # only ever called once, at initialization
        while self._working:
            task, _ = await asyncio.gather(self._get_task(), self._acquire_worker())
            asyncio.create_task(task.execute(self._mark_done))

    async def execute(self, task: Task):
        if not self._working:
            raise RuntimeError("WorkerPool shutdown")

        delayed_task = DelayedTask(task)
        self._put_task(delayed_task)
        return await delayed_task.result()

    async def shutdown(self):
        self._working = False
        for task in self._queue:
            task.future.set_exception(asyncio.CancelledError("WorkerPool shutdown"))



@contextmanager
def worker_pool(size: int | None = None, rate: float | None = None):
    try:
        workers = WorkerPool(size, rate)
        yield workers
    finally:
        asyncio.create_task(workers.shutdown(), name=f'{workers.__class__.__name__}.{workers.__class__.shutdown.__name__}')
