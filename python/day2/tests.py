#!/usr/bin/env python3

from day2 import *

commands: list[str] = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

values = getDepthHorizontalValues(commands)

assert(values["horizontal"] == 15 and values["depth"] == 10)
assert(calculateDepthHorizontalMultiple(commands) == 150)
