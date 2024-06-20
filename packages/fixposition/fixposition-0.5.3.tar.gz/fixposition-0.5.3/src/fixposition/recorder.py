#!/usr/bin/env python3
"""
Record messages to file

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

import asyncio
import logging
import time
from fixposition import receiver

log = logging.getLogger("recorder")


async def record(
    msg_q: asyncio.Queue[bytes], filename: str = "fpx_messages.txt"
) -> None:

    log.info(f"Recording messages to {filename}")

    with open(filename, "ab") as f:  # Open file in binary append mode
        while True:
            message = await msg_q.get()
            timestamp = time.time()
            timestamped_message = f"{timestamp:.3f} ".encode() + message
            f.write(timestamped_message)
            msg_q.task_done()


async def main(filename: str, host: str = "localhost") -> None:
    """record messages to file"""
    msg_q: asyncio.Queue[bytes] = asyncio.Queue()

    async with asyncio.TaskGroup() as tg:
        tg.create_task(record(msg_q, filename))
        tg.create_task(receiver.receive(host, out_q=msg_q))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main("fpx_messages.txt"))
    except KeyboardInterrupt:
        print("done.")
