#!/usr/bin/env python3
"""
 Send mock gps data.

 Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

import asyncio
from roxbot.utils.runners import run_main_async
from fixposition.gps_node import FpxNode
from rox_bridge import bridge_node


async def rotate_heading(node: FpxNode) -> None:
    while True:
        node.heading += 1
        await asyncio.sleep(0.1)


async def main() -> None:

    node = FpxNode(mock=True)

    async with asyncio.TaskGroup() as tg:
        tg.create_task(bridge_node.main())
        tg.create_task(node.main())
        tg.create_task(rotate_heading(node))


if __name__ == "__main__":
    run_main_async(main())
