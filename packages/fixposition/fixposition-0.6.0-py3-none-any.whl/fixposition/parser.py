#!/usr/bin/env python3
"""
main parsing code

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

from typing import TypeAlias, List

from .messages import gga, hdt, odometry
from .messages import GgaData, HdtData, OdometryData

FPX_Message: TypeAlias = GgaData | HdtData | OdometryData


# pylint: disable=dangerous-default-value
def parse(msg: str, ignore: List[str] = []) -> FPX_Message | None:
    """
    Parse messages, return parsed data or None if message is not recognized or ignored.

    Parameters:
    msg (str): The message to be parsed.
    ignore (List[str]): A list of message types to ignore. Default is an empty list.
                        This is intentionally set as a mutable default argument for performance reasons.

    Returns:
    FPX_Message | None: The parsed message data or None if the message is not recognized or ignored.
    """
    if msg.startswith("$GPGGA") and "GGA" not in ignore:
        return gga.parse(msg)

    if msg.startswith("$GPHDT") and "HDT" not in ignore:
        return hdt.parse(msg)

    if msg.startswith("$FP,ODOMETRY") and "ODOM" not in ignore:
        return odometry.parse(msg)

    return None
