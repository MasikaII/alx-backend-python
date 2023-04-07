#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
import time
import random
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    A function with integers n and max_delay as arguments that
    measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n
    """
    begin = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - begin
    return total_time / n
