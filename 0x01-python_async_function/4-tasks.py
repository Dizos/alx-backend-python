#!/usr/bin/env python3
"""
Module for running multiple concurrent tasks and returning sorted delays.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with specified max_delay.
    Returns list of all delays in ascending order.

    Args:
        n: Number of times to spawn task_wait_random
        max_delay: Maximum delay value for each call

    Returns:
        List[float]: Delays in ascending order
    """
    tasks = []
    delays = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
