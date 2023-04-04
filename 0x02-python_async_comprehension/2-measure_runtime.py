#!/usr/bin/env python3
"""
Using asyncio.gather
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures and returns total runtime
    """
    start = time.perf_counter()
    task = [asyncio.create_task(async_comprehension()) for i in range(4)]
    result = await asyncio.gather(*task)
    total_time = time.perf_counter() - start
    return total_time
