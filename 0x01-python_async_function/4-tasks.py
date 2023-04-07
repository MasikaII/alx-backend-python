#!/usr/bin/env python3
"""Tasks"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    A new function task_wait_n
    """
    tasks_delayed: List[float] = []
    for i in range(n):
        tasks_delayed.append(await task_wait_random(max_delay))
    return sorted(tasks_delayed)
