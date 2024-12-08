"""
--- Day 7: Bridge Repair ---

https://adventofcode.com/2024/day/7
"""

def get_inputs() -> list[tuple[int,list[int]]]:
    lines = []
    with open("inputs/day7.txt") as f:
        while line := f.readline().strip():
            value, inputs = line.split(':')
            inputs = map(int, inputs.split())
            lines.append((int(value), list(inputs)))

    return lines

def solve(target: int, values: list[int], operations) -> bool:
    state = {0: {values[0]}}

    for pos in range(1, len(values)):
        state[pos] = set()
        for value in state[pos - 1]:
            for op in operations:
                state[pos].add(op(value, values[pos]))

    return target in state[len(values) - 1]


def solve_p1(target: int, values: list[int]) -> bool:
    operations = [
        lambda v1, v2: v1+v2,
        lambda v1, v2: v1*v2,
    ]

    return solve(target, values, operations)

def solve_p2(target: int, values: list[int]) -> bool:
    operations = [
        lambda v1, v2: v1+v2,
        lambda v1, v2: v1*v2,
        lambda v1, v2: int(f'{v1}{v2}')
    ]

    return solve(target, values, operations)

def calibration_results(solver, lines: list[tuple[int,list[int]]]) -> int:
    total = 0
    for target, values in lines:
        if solver(target, values):
            total += target

    return total



def main():
    print(f"Part 1: {calibration_results(solve_p1, get_inputs())}")
    print(f"Part 2: {calibration_results(solve_p2, get_inputs())}")