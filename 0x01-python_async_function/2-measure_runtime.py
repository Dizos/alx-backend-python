#!/usr/bin/env python3
"""
Module for measuring the average execution time of concurrent coroutines.
"""

import asyncio
import time
from typing import float
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time per task for wait_n(n, max_delay).

    Args:
        n: Number of concurrent tasks
        max_delay: Maximum delay for each task

    Returns:
        float: Average execution time per task
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    
    total_time = end_time - start_time
    return total_time / n
