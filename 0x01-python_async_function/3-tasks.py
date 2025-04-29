#!/usr/bin/env python3
"""
This module provides a function to create an asyncio.Task from the wait_random coroutine.
"""

import asyncio
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for the wait_random coroutine with the specified max_delay.

    Args:
        max_delay (int): Maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: A task object representing the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
