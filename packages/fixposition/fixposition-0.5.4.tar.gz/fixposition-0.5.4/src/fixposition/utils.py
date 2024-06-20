#!/usr/bin/env python3
"""
 utility functions

 Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

import time


def timestamp() -> float:
    return round(time.time(), 3)
