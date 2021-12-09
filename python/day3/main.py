#!/usr/bin/env python3

def generate_bit_number_with_most_common_ones_in_bits(binary_numbers: list[str]) -> str:
    binary_number = ""

    for d in range(len(binary_numbers[0])):
        binary_number += str(get_most_common_bit(binary_numbers, d, 1))

    return binary_number

def get_most_common_bit(binary_numbers: list[str], index: int, tiebreak: int) -> int:
    ones_count = count_ones_in_column(binary_numbers, index)
    half_of_total = len(binary_numbers) / 2

    if (ones_count == half_of_total):
        return tiebreak

    if (ones_count < half_of_total):
        return 0

    return 1

def get_least_common_bit(binary_numbers: list[str], index: int, tiebreak: int) -> int:
    ones_count = count_ones_in_column(binary_numbers, index)
    half_of_total = len(binary_numbers) / 2

    if (ones_count == half_of_total):
        return tiebreak

    if (ones_count > half_of_total):
        return 0

    return 1

def count_ones_in_column(binary_numbers: list[str], index: int) -> int:
    assert index < len(binary_numbers[0]), 'Index of list should be below of ' + str(len(binary_numbers[0]))

    count_ones_in_column = 0

    for number in binary_numbers:
        if (number[index] == "1"):
            count_ones_in_column += 1

    return int(count_ones_in_column)

def invert_bits(binary_number: str) -> str:
    binary_number_without_prefix = bin(binary_number)[2:]

    binary_number = ""
    for i in binary_number_without_prefix:
        binary_number += invert_bit(i)

    return binary_number

def invert_bit(bit: str) -> str:
    if bit == "0":
        return "1"

    return "0"

def get_gamma_rate(binary_numbers: list[str]) -> int:
    return int(generate_bit_number_with_most_common_ones_in_bits(binary_numbers), 2)

def get_epsilon_rate(gamma_rate: int) -> int:
    return int(invert_bits(gamma_rate), 2)

def filter_by_column(binary_numbers: list[str], criteria: callable, index: int = 0) -> list[str]:
    numbers_filtered = list()

    for number in binary_numbers:
        if (criteria(binary_numbers, number, index)):
            numbers_filtered.append(number)

    if (len(numbers_filtered) == 1 or index + 1 >= len(binary_numbers[0])):
        return numbers_filtered

    return filter_by_column(numbers_filtered, criteria, index + 1)

def get_oxygen_generator_rate(binary_numbers: list[str]) -> int:
    numbers_filtered = filter_by_column(
        binary_numbers,
        lambda binary_numbers, number, index : number[index] == str(get_most_common_bit(binary_numbers, index, 1))
    )

    assert len(numbers_filtered) == 1, 'should be only one number filtered in the end!'

    return int(numbers_filtered[0], 2)

def get_co2_scrubber_rate(binary_numbers: list[str]) -> int:
    numbers_filtered = filter_by_column(
        binary_numbers,
        lambda binary_numbers, number, index : number[index] == str(get_least_common_bit(binary_numbers, index, 0))
    )

    assert len(numbers_filtered) == 1, 'should be only one number filtered in the end!'

    return int(numbers_filtered[0], 2)

if __name__ == '__main__':
    fo = open("../../assets/day3/input.txt")
    file_lines = fo.read().splitlines()
    fo.close()

    gamma_rate = get_gamma_rate(file_lines)
    print("Power consumption: " + str(gamma_rate * get_epsilon_rate(gamma_rate)))

    print("Support rating: " + str(get_oxygen_generator_rate(file_lines) * get_co2_scrubber_rate(file_lines)))
