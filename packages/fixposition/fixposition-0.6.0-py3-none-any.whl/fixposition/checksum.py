#!/usr/bin/env python3
"""
checksum of nnmea messages

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

from typing import Callable, TypeVar, Any
from functools import wraps

# Define a type variable for the return type of the decorated function
T = TypeVar("T")


def calculate_checksum(nmea_str: str) -> str:
    checksum = 0
    for char in nmea_str:
        checksum ^= ord(char)
    return f"{checksum:02X}"


def check_checksum(message: str) -> None:
    """check message checksum, raise ValueError if invalid"""
    # Attempt to split the message to extract checksum and payload
    asterisk_position = message.find("*")
    if asterisk_position == -1:
        raise ValueError("Invalid message format: no checksum")

    provided_checksum = message[asterisk_position + 1 : asterisk_position + 3]
    payload = message[1:asterisk_position]  # Exclude the '$' character and after '*'

    # Use a more efficient way to calculate the XOR value of all payload characters
    calculated_checksum = 0
    for char in payload:
        calculated_checksum ^= ord(char)
    calculated_checksum_hex = (
        f"{calculated_checksum:02X}"  # Convert to two-digit hexadecimal
    )

    # Compare the provided checksum with the calculated checksum
    if not provided_checksum.upper() == calculated_checksum_hex:
        raise ValueError("Invalid message format: checksum mismatch")


def validate_checksum(func: Callable[[str], T]) -> Callable[[str], T]:
    @wraps(func)
    def wrapper(message: str, *args: Any, **kwargs: Any) -> T:
        # First, check the checksum of the message
        check_checksum(message)

        # If checksum is valid, proceed to the original function
        return func(message, *args, **kwargs)

    return wrapper
