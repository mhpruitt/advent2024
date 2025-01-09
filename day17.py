"""
--- Day 16: Chronospatial Computer ---

https://adventofcode.com/2024/day/17
Needed help with part 2, credit to u/erisdottir
"""

from dataclasses import dataclass, field
from typing import Iterable


@dataclass
class Computer:
    a: int = 0
    b: int = 0
    c: int = 0
    ip: int = 0
    output: list[int] = field(default_factory=list)

    def from_combo(self, operand: int) -> int:
        match operand:
            case operand if 0 <= operand <= 3:
                return operand
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
            case _:
                raise ValueError(f"Invalid combo operand: {operand}")

    def exec(self, program: list[int]) -> bool:
        if self.ip >= len(program):
            return False

        opcode = program[self.ip]
        operand = program[self.ip + 1]

        match opcode:
            case 0:  # adv
                divisor = 2 ** self.from_combo(operand)
                self.a //= divisor

            case 1:  # bxl
                self.b ^= operand

            case 2:  # bst
                self.b = self.from_combo(operand) % 8

            case 3:  # jnz
                if self.a != 0:
                    self.ip = operand
                    return True

            case 4:  # bxc
                self.b ^= self.c

            case 5:  # out
                value = self.from_combo(operand) % 8
                self.output.append(value)

            case 6:  # bdv
                divisor = 2 ** self.from_combo(operand)
                self.b = self.a // divisor

            case 7:  # cdv
                divisor = 2 ** self.from_combo(operand)
                self.c = self.a // divisor

            case _:
                raise ValueError(f"Invalid opcode: {opcode}")

        self.ip += 2
        return True

    def run(self, program: list[int]) -> list[int]:
        while self.exec(program):
            pass

        return self.output


def find_self_replicating_a(program: list[int]) -> int | None:
    def workhorse(fixed: int, place: int) -> int | None:
        for digit in range(8):
            # Combine previously found digits with current trial digit
            val = fixed + (digit << ((15 - place) * 3))

            # Run program with this value of A
            output = Computer(a=val).run(program)

            # Check if we've found complete solution
            if output == program:
                return val

            # Check if rightmost portion matches (we build right-to-left)
            if output[-(place + 1):] == program[-(place + 1):]:
                # This digit looks promising, try to build rest of solution
                result = workhorse(val, place + 1)
                if result is not None:
                    return result

    return workhorse(0, 0)


def load_input() -> list[str]:
    with open("inputs/day17.txt") as f:
        return f.readlines()


type Day17Input = tuple[int, int, int, list[int]]
def parse_input(problem_input: Iterable[str]) -> Day17Input:
    lines = [line.strip() for line in problem_input]

    register_a = int(lines[0].split(":")[1].strip())
    register_b = int(lines[1].split(":")[1].strip())
    register_c = int(lines[2].split(":")[1].strip())
    program = list(map(int, lines[4].split(":")[1].strip().split(",")))

    return register_a, register_b, register_c, program


def main():
    a, b, c, program = parse_input(load_input())
    computer = Computer(a, b, c)

    print(f"Part 1: {computer.run(program)}")
    print(f"Part 2: {find_self_replicating_a(program)}")

