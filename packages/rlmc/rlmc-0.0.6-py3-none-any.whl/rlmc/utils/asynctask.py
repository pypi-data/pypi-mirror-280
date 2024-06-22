"""
@File    :   asynctask.py
@Time    :   2024/06/21 13:08:38
@Author  :   RayLam
@Contact :   1027196450@qq.com
"""

import sys

sys.path.append(".")

import asyncio
import contextvars
import functools
import time


from rlmc.utils.logger import Logger


python_version = f"{sys.version_info.major}.{sys.version_info.minor}"


# ---------python3.8 没有asyncio.to_thread，此处支持python3.8--------*
async def to_thread(func, *args, **kwargs):
    loop = asyncio.get_running_loop()
    ctx = contextvars.copy_context()
    func_call = functools.partial(ctx.run, func, *args, **kwargs)
    return await loop.run_in_executor(None, func_call)


try:
    import asyncio.to_thread as async_to_thread
except:
    async_to_thread = to_thread

# ---------python3.8 没有asyncio.to_thread，此处支持python3.8--------*

__all__ = ["AsyncTasks"]

logger = Logger(__name__, level=Logger.DEBUG)


class AsyncTasks:
    def __init__(self, semaphore_num):
        self.semaphore_num = semaphore_num

    async def async_wrapper(self, sync_func, *args, **kwargs):
        coroutine = await async_to_thread(sync_func, *args, **kwargs)
        return coroutine

    async def create_task(self, sync_func, *args, **kwargs):
        task = await asyncio.create_task(self.async_wrapper(sync_func, *args, **kwargs))
        return task

    async def semaphore(
        self, semaphore, task
    ):  # 控制异步并发数，with semaphore要套每个task
        async with semaphore:
            return await task

    async def main(self, *tasks):
        semaphore = asyncio.Semaphore(self.semaphore_num)  # semaphore初始化要在gather前
        tasks = [self.semaphore(semaphore, task) for task in tasks]
        res = await asyncio.gather(*tasks)
        return res


# 一个原同步函数
def sync_task(interval, num):
    time.sleep(interval)
    return f"task_{interval + num}"


# 一个异步函数
# async def async_task(sync_task, *args, **kwargs):
#     task = asyncio.to_thread(sync_task, *args, **kwargs)
#     res = await task
#     return res


# async def main():
#     print("main start")

#     task1 = asyncio.create_task(async_task(sync_task, 1))

#     task2 = asyncio.create_task(async_task(sync_task, 2))

#     print("main end")

#     ret1 = await task1
#     ret2 = await task2
#     print(ret1, ret2)


if __name__ == "__main__":
    start = time.time()
    # asyncio.run(main())

    asynctasks = AsyncTasks(semaphore_num=2)
    task1 = asynctasks.create_task(sync_task, 2, 9)
    task2 = asynctasks.create_task(sync_task, 2, 9)
    task3 = asynctasks.create_task(sync_task, 3, 6)

    main = asynctasks.main(task1, task2, task3)
    res = asyncio.run(main)
    print(res)
    print(time.time() - start)

    start = time.time()
    print(sync_task(2, 9))
    print(sync_task(2, 9))
    print(sync_task(3, 6))
    print(time.time() - start)
