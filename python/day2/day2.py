#!/usr/bin/env python3

from typing import Dict

def getDepthHorizontalValues(commands: list[str]) -> Dict[str, int]:
    depth: int = 0
    horizontal: int = 0

    for command in commands:
        instruction = command.split(" ")
        operator = instruction[0]
        operand = instruction[1]

        if operator == "forward":
            horizontal += int(operand)
        elif operator == "up":
            depth -= int(operand)
        elif operator == "down":
            depth += int(operand)
        else:
            assert 0 and "Operator %s not found", operator

    return {
        "depth": depth,
        "horizontal": horizontal,
    }

def calculateDepthHorizontalMultiple(commands: list[str]) -> int:
    values = getDepthHorizontalValues(commands)

    return values["horizontal"] * values["depth"]

if __name__ == '__main__':
    fo = open("../../assets/day2/input.txt")
    fileLines = fo.read().splitlines()
    fo.close()

    print("Depth x Horizontal: " + str(calculateDepthHorizontalMultiple(fileLines)))
