#!/usr/bin/env python3
"""
Module: 2-measure_runtime
Measures the runtime of executing async_comprehension four times in parallel.
"""

import asyncio
import time
from typing import List
from importlib import import_module

async_comprehension = import_module('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
