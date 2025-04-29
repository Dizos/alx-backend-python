#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine that spawns multiple wait_random coroutines
and returns their delays in ascending order.
"""

import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns a list of delays
    in ascending order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for each wait_random call.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for delay in await asyncio.gather(*tasks):
        # Insert delay in ascending order without sort()
        inserted = False
        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)
    return delays
