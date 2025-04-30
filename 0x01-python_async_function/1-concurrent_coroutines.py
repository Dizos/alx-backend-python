#!/usr/bin/env python3
"""
Module for running multiple concurrent coroutines and returning sorted delays.
"""

import asyncio
from typing import List
from 0-basic_async_syntax.py import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns the list of all the delays in ascending order.

    Args:
        n: Number of times to spawn wait_random
        max_delay: Maximum delay value for each wait_random call

    Returns:
        List[float]: List of delays in ascending order
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays
