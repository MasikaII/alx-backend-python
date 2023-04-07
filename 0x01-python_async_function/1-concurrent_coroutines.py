#!/usr/bin/env python3
"""Multiple coroutines with async"""


import asyncio
from typing import TYPE_CHECKING, List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    An async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay.
    Spawns wait_random n times with the specified max_delay
    """
    task = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    output = await asyncio.gather(*task)
    return sorted(output)
