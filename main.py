import asyncio
from util import async_timed, delay
import requests
import functools


@async_timed()
async def youtube() -> None:
    main_loop = asyncio.get_event_loop()
    main_loop.run_in_executor(None, functools.partial(requests.get, url="https://www.youtube.com/"))


@async_timed()
async def main():
    tasks = []
    for i in range(100):
        tasks.append(asyncio.create_task(youtube()))

    for task in tasks:
        await task

asyncio.run(main(), debug=True)