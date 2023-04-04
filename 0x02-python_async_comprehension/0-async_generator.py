#!/usr/bin/env python3
"""
Async Generator
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    A coroutine that takes no argument and loops 10 times, each time asynchronously waits 1 second
    """
    for a in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
