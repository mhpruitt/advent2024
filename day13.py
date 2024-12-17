"""
--- Day 13: Claw Contraption ---

https://adventofcode.com/2024/day/13
"""

from dataclasses import dataclass
from math import gcd, ceil, floor

@dataclass
class ClawMachine:
    button_a: tuple[int, int]
    button_b: tuple[int, int]
    prize: tuple[int, int]

    def find_minimal_solution(self: 'ClawMachine') -> tuple[int | None, int | None, int | None]:
        ax, ay = self.button_a
        bx, by = self.button_b
        px, py = self.prize

        # Solve for X
        x_sol = solve_diophantine(ax, bx, px)
        if not x_sol:
            return None, None, None

        x0, y0, dx, dy = x_sol

        # Sub into Y and check if this equation has a solution
        y_check = ay * dx + by * dy
        if y_check == 0:
            # check if particular solution works
            if ay * x0 + by * y0 == py:
                # Find k that minimizes cost with non-negative solutions
                k_min_a = ceil(-x0 / dx) if dx > 0 else floor(-x0 / dx)
                k_min_b = ceil(-y0 / dy) if dy > 0 else floor(-y0 / dy)
                k = max(k_min_a, k_min_b)
                a = x0 + k * dx
                b = y0 + k * dy

                return int(a), int(b), int(3 * a + b)

            return None, None, None

        # Solve for k
        k = (py - (ay * x0 + by * y0)) / (ay * dx + by * dy)
        if not k.is_integer():
            return None, None, None

        k = int(k)

        # Get base solution
        a = x0 + k * dx
        b = y0 + k * dy

        # If negative, shift the solution
        if dx == 0 and dy == 0:
            if a >= 0 and b >= 0:
                return int(a), int(b), int(3 * a + b)

            return None, None, None

        if dx == 0:
            steps = ceil(-b / dy) if dy > 0 else floor(-b / dy)
            a = x0 + (k + steps) * dx
            b = y0 + (k + steps) * dy
        elif dy == 0:
            steps = ceil(-a / dx) if dx > 0 else floor(-a / dx)
            a = x0 + (k + steps) * dx
            b = y0 + (k + steps) * dy
        else:
            lcm = abs(dx * dy) // gcd(dx, dy)
            # Find minimal non-negative solution
            for i in range(abs(lcm)):
                new_a = a + i * dx
                new_b = b + i * dy
                if new_a >= 0 and new_b >= 0:
                    return int(new_a), int(new_b), int(3 * new_a + new_b)

            return None, None, None

        if a >= 0 and b >= 0:
            return int(a), int(b), int(3 * a + b)

        return None, None, None


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return b, 0, 1

    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return g, x, y


def solve_diophantine(a: int, b: int, c: int) -> tuple[int, int, int, int] | None:
    if a == 0 and b == 0:
        return (0, 0, 0, 0) if c == 0 else None

    g, x0, y0 = extended_gcd(abs(a), abs(b))

    if c % g != 0:  # No solution exists
        return None

    # Scale the solution
    x0 *= c // g
    y0 *= c // g

    # Adjust signs
    if a < 0: x0 = -x0
    if b < 0: y0 = -y0

    # Return specific and general solution components
    return x0, y0, b // g, -a // g



def get_claw_machines():
    with open('inputs/day13.txt') as f:
        return [line.strip() for line in f if line.strip()]


def parse_claw_machines(claw_machines, offset=0):
    machines = []
    current = []

    def parse_claw_machine_line(token1, token2, l, o=0):
        x = int(l.split(token1)[1].split(',')[0]) + o
        y = int(l.split(token2)[1]) + o
        current.append((x, y))

    for line in claw_machines:
        line = line.strip()
        if line.startswith('Button A:'):
            parse_claw_machine_line('X+', 'Y+', line)
        elif line.startswith('Button B:'):
            parse_claw_machine_line('X+', 'Y+', line)
        elif line.startswith('Prize:'):
            parse_claw_machine_line('X=', 'Y=', line, offset)

            if len(current) == 3:
                machines.append(ClawMachine(*current))
                current = []

    return machines


def calc_total_tokens(machines):
    solutions = [machine.find_minimal_solution() for machine in machines]
    return sum(s[2] for s in solutions if s[2])


def main():
    raw_claw_machines = get_claw_machines()

    machines_p1 = parse_claw_machines(raw_claw_machines)
    print(f"Part 1: {calc_total_tokens(machines_p1)}")

    machines_p2 = parse_claw_machines(raw_claw_machines, 10000000000000)
    print(f"Part 2: {calc_total_tokens(machines_p2)}")
