#!/usr/bin/env python3
"""
using asyncio.gather
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures and returns total runtime
    """
    begin = time.perf_counter()
    chore = [asyncio.create_chore(async_comprehension()) for i in range(4)]
    result = await asyncio.gather(*chore)
    aggregate_time = time.perf_counter() - begin
    return aggregate_time
