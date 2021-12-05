#!/usr/bin/env python

def count_large_measurements(values: list[int]) -> int:
    larger_values: int = 0
    for i in range(1, len(values)):
        assert isinstance(values[i], int) and isinstance(values[i - 1], int), "All values should be integer!"

        if values[i] > values[i - 1]:
            larger_values += 1

    return larger_values

def get_large_measurements_in_slidding_window(values: list[int]) -> list[int]:
    new_values: list[int] = list()

    for i in range(2, len(values)):
        assert isinstance(values[i], int) \
            and isinstance(values[i - 1], int) \
            and isinstance(values[i - 2], int), \
            "All values should be integer!"

        new_values.append(values[i] + values[i - 1] + values[i - 2])

    return new_values

def count_large_measurements_in_slidding_window(values: list[int]) -> int:
    return count_large_measurements(get_large_measurements_in_slidding_window(values))

if __name__ == '__main__':
    fo = open("../../assets/day1/input.txt")
    file_lines = list(map(int, fo.read().splitlines()))
    fo.close()

    print("larger measurements: " + str(count_large_measurements(file_lines)))
    print("larger in sliding window measurements: " + str(count_large_measurements_in_slidding_window(file_lines)))
    print("total of lines: " + str(len(file_lines)))
