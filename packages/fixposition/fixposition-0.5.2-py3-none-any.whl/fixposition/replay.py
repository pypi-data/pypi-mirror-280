#!/usr/bin/env python3
"""
 replay pre-recorded timestamped data

 Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""
import asyncio
import io
import logging
from typing import IO, Optional

from fixposition.test_data import DATA_LOG

log = logging.getLogger("replay")


def parse_line(line: str) -> tuple[float, str]:
    """parse timestamp and message from line"""
    timestamp, message = line.split(" ", 1)
    return float(timestamp), message


# pylint: disable=unused-argument
async def handle_client(
    reader: asyncio.StreamReader, writer: asyncio.StreamWriter, data: IO[str]
) -> None:
    addr = writer.get_extra_info("peername")
    log.info(f"Connection from {addr}")

    try:
        # loop forever
        ts: float | None = None  # player time

        while True:
            for line in data:
                line_ts, message = parse_line(line)

                # calculate delay
                if ts is None:
                    ts = line_ts
                else:
                    delay = line_ts - ts
                    ts = line_ts
                    await asyncio.sleep(delay)
                writer.write(message.encode())
                await writer.drain()

            log.info("restarting replay")
            data.seek(0)
    except (asyncio.CancelledError, ConnectionResetError, BrokenPipeError):
        log.info("unexpected close of connection")
    finally:
        # writer.close()
        # await writer.wait_closed()
        data.seek(0)  # rewind data
        log.info(f"Closed connection from {addr}")


async def start_server(data: IO[str], port: int = 21000) -> None:
    async def client_handler(
        reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
        await handle_client(reader, writer, data)

    server = await asyncio.start_server(client_handler, "localhost", port)
    addr = server.sockets[0].getsockname()
    log.info(f"Serving on {addr}")

    async with server:
        await server.serve_forever()


async def main(filename: Optional[str] = None) -> None:
    """replay file or test data if filename is None"""
    if filename is not None:
        log.info(f"replaying data from {filename}")
        with open(filename, "r", encoding="utf-8") as file:
            data = io.StringIO(file.read())
    else:
        log.info("replaying default data")
        data = io.StringIO(DATA_LOG)

    await start_server(data)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        import sys

        data_file = sys.argv[1] if len(sys.argv) > 1 else None
        asyncio.run(main(data_file))
    except KeyboardInterrupt:
        print("done.")
