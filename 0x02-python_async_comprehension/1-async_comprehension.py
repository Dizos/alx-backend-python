#!/usr/bin/env python3
"""
Module: 1-async_comprehension
Demonstrates asynchronous comprehensions with an async generator.
"""

from typing import List
from importlib import import_module

async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension.

    This coroutine uses an async comprehension to iterate over the async_generator,
    collecting 10 random floats between 0 and 10.

    Returns:
        List[float]: A list of 10 random floats.
    """
    return [num async for num in async_generator()]
