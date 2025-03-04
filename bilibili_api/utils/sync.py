"""
bilibili_api.utils.sync

同步执行异步函数
"""

from typing import Coroutine
import asyncio
from .. import settings


def __ensure_event_loop():
    try:
        asyncio.get_event_loop()

    except:
        asyncio.set_event_loop(asyncio.new_event_loop())


def sync(coroutine: Coroutine):
    """
    同步执行异步函数，使用可参考 [同步执行异步代码](https://nemo2011.github.io/bilibili-api/#/sync-executor)

    Args:
        coroutine (Coroutine): 异步函数

    Returns:
        该异步函数的返回值
    """
    __ensure_event_loop()
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(coroutine)
