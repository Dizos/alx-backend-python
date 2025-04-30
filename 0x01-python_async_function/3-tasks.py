#!/usr/bin/env python3
"""
Module for creating asyncio tasks from coroutines.
"""

import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio Task from the wait_random coroutine.

    Args:
        max_delay: Maximum delay for the wait_random coroutine

    Returns:
        asyncio.Task: Task object for the wait_random coroutine
    """
    return asyncio.create_task(wait_random(max_delay))
