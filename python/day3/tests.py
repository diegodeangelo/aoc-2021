#!/usr/bin/env python3

from main import *

report = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

# FIRST PART

# Verify if gamma and epsilon rates are right
gamma_rate = get_gamma_rate(report)

assert gamma_rate == 22
assert get_epsilon_rate(gamma_rate) == 9

# SECOND PART

# Verify if oxygen generator and co2 scrubber rates are right
oxygen_generator_rate = get_oxygen_generator_rate(report)
co2_scrubber_rate = get_co2_scrubber_rate(report)

assert oxygen_generator_rate == 23
assert co2_scrubber_rate == 10
