"""
--- Day 3: Mull It Over ---

https://adventofcode.com/2024/day/3
"""
import re


def get_program_memory():
    lines = []
    with open("inputs/day3.txt") as f:
        while line := f.readline().strip():
            lines.append(line)
    return ''.join(lines)

# Part 1
def sum_multiplications(program):
    mul_extractor = re.compile(r"mul\((-?\d+),(-?\d+)\)")
    operands = mul_extractor.findall(program)
    return sum([int(o1) * int(o2) for o1, o2 in operands])

# Part 2
def conditionally_sum_multiplications(program):
    extractor = re.compile(r"(mul\((-?\d+),(-?\d+)\))|(do\(\))|(don't\(\))")
    instructions = extractor.findall(program)

    sum_enabled = True
    running_total = 0

    for mul_group, o1, o2, do, dont in instructions:
        if mul_group and sum_enabled:
            running_total += int(o1) * int(o2)
        elif do:
            sum_enabled = True
        elif dont:
            sum_enabled = False

    return running_total

def main():
    print(f'Part 1: {sum_multiplications(get_program_memory())}')
    print(f'Part 2: {conditionally_sum_multiplications(get_program_memory())}')
