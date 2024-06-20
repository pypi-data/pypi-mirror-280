#!/usr/bin/env python3
"""
 receiver code for fixposition messages

 Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

import asyncio

import logging


log = logging.getLogger("receiver")


async def receive(
    host: str = "localhost",
    port: int = 21000,
    out_q: asyncio.Queue[bytes] | None = None,
    printout: bool = False,
) -> None:
    """receive messages from fixposition over socket, and put them in a queue

    Args:
        host (str, optional): fixpositon server. Defaults to "localhost".
        port (int, optional): socket port. Defaults to 21000.
        out_q (asyncio.Queue | None, optional): queue to put messages into. Defaults to None.
        printout (bool, optional): print messages to stdout. Defaults to False.
    """
    reader, writer = await asyncio.open_connection(host, port)

    log.info(f"Connected to {host}:{port}")

    try:
        while True:
            data = await reader.readline()
            log.debug(f"<{data!r}")
            if not data:
                break

            if out_q:
                await out_q.put(data)

            if printout:
                print(data)

    except asyncio.CancelledError:
        pass
    finally:
        writer.close()
        await writer.wait_closed()

    log.info("Connection closed")
