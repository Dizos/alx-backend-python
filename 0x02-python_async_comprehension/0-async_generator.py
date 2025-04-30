#!/usr/bin/env python3
"""
Module: 0-async_generator
Contains an asynchronous generator that yields random numbers.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    This coroutine loops 10 times, each time waiting asynchronously for 1 second,
    then yielding a random float between 0 and 10.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
