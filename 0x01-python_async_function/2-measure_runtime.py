#!/usr/bin/env python3
"""
This module provides a function to measure the average execution time
of the wait_n coroutine.
"""

import asyncio
import time
from concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns
    the average time per call.

    Args:
        n (int): Number of times to spawn wait_n.
        max_delay (int): Maximum delay for each wait_n call.

    Returns:
        float: Average execution time per call (total_time / n).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
