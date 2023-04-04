#!/usr/bin/env python3
"""
coroutine called async_comprehension
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers, returns 10 random numbers 
    """
    numRand = [intRand async for intRand in async_generator()]
    return numRand

