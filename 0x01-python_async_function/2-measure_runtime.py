#!/usr/bin/env python3
"""
Module for measuring the average execution time of wait_n.
"""

import asyncio
import time
from typing import float
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time per coroutine for wait_n(n, max_delay).

    Args:
        n: Number of coroutines to execute
        max_delay: Maximum delay for each coroutine

    Returns:
        float: Average execution time per coroutine
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    
    total_time = end_time - start_time
    return total_time / n
