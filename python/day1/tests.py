#!/usr/bin/env python

from main import *

measurements: list[int] = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

assert count_large_measurements(measurements) == 7

assert get_large_measurements_in_slidding_window(measurements) == [607, 618, 618, 617, 647, 716, 769, 792]
assert count_large_measurements_in_slidding_window(measurements) == 5

