#!/usr/bin/env python3
"""
Module for creating asyncio Tasks from wait_random coroutine.
"""

import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio Task for wait_random(max_delay).

    Args:
        max_delay: Maximum delay for wait_random

    Returns:
        asyncio.Task: Task object for wait_random
    """
    return asyncio.create_task(wait_random(max_delay))
