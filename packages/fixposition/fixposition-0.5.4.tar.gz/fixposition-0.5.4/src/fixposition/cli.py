#!/usr/bin/env python3
"""
 main cli file

 Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

import asyncio
import logging
import os
from datetime import datetime
from typing import Coroutine

import click
import coloredlogs
from roxbot.utils import run_main_async

from fixposition import __version__

LOG_FORMAT = "%(asctime)s.%(msecs)03d [%(name)s] %(filename)s:%(lineno)d - %(message)s"
loglevel = os.environ.get("LOGLEVEL", "INFO").upper()
coloredlogs.install(level=loglevel, fmt=LOG_FORMAT)
logging.info(f"Log level set to {loglevel}")


# --------------helper functions
def generate_default_filename() -> str:
    """Generate a default filename with a timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"fpx_{timestamp}.txt"


def run_async(coro: Coroutine) -> None:
    """Run an async function in the main thread."""
    try:
        asyncio.run(coro)
    except KeyboardInterrupt:
        print("done.")


# -------------cli commands


@click.group()
@click.version_option(version=__version__)
def cli() -> None:
    pass  # pragma: no cover


@cli.command("node")
def start_node() -> None:
    """Start the gps node"""

    from fixposition.gps_node import FpxNode

    node = FpxNode()
    run_main_async(node.main())


@cli.command()
@click.option(
    "--host",
    default="localhost",
    help="Host to listen on.",
)
def listen(host: str) -> None:
    """Listen to messages and print them to stdout"""

    from fixposition import receiver

    run_async(receiver.receive(host, printout=True))


@cli.command()
@click.option(
    "--filename", default=None, help="Name of the file to record messages to."
)
@click.option(
    "--host",
    default="localhost",
    help="Host to listen on.",
)
def record(filename: str, host: str) -> None:
    """Record messages to file"""

    from fixposition import recorder

    if filename is None:
        filename = generate_default_filename()
    print(f"Recording messages to {filename}")

    run_async(recorder.main(filename, host))


@cli.command("replay")
@click.option("--filename", default=None, help="Name of the file to replay.")
def replay_messages(filename: str) -> None:
    """Replay messages from a file or default data if not provided."""

    from fixposition import replay

    run_async(replay.main(filename))


if __name__ == "__main__":
    cli()  # pragma: no cover
