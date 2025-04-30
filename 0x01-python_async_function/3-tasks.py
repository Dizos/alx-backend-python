#!/usr/bin/env python3
"""
Module for creating asyncio Tasks from wait_random coroutine.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio Task for wait_random(max_delay).

    Args:
        max_delay: Maximum delay for wait_random

    Returns:
        asyncio.Task: Task object for wait_random
    """
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
