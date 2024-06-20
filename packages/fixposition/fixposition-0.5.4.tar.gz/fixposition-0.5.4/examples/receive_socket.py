#!/usr/bin/env python3
"""
receive data stream from fixposition

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

import asyncio
import socket


HOST = "localhost"
PORT = 21000


def listen(host: str, port: int) -> None:
    # This is not a robust, NMEA compliant parser. DO NOT use in production code
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            data = s.recv(1024)
            print(data)
            # data_str = data.decode(errors="ignore").strip()
            # print(data_str)


if __name__ == "__main__":
    try:
        asyncio.run(listen(HOST, PORT))  # type: ignore
    except KeyboardInterrupt:
        print("done.")
