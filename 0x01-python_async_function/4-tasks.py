#!/usr/bin/env python3
"""
Module for running multiple concurrent tasks and returning sorted delays.
"""

import asyncio
from typing import List
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.
    Returns the list of all the delays in ascending order.

    Args:
        n: Number of times to spawn task_wait_random
        max_delay: Maximum delay value for each task_wait_random call

    Returns:
        List[float]: List of delays in ascending order
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays
