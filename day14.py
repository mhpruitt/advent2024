"""
--- Day 14: Restroom Redoubt ---

https://adventofcode.com/2024/day/14
"""

import re
from math import prod, log2
from dataclasses import dataclass
from collections import Counter

@dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int

    def position_at(self, steps, width, height):
        x = (self.px + self.vx * steps) % width
        y = (self.py + self.vy * steps) % height
        return x, y

    def part1_position(self, steps, width, height):
        final_x, final_y = self.position_at(steps, width, height)

        left = final_x < width // 2
        top = final_y < height // 2

        quadrant = (
            0 if final_x == width // 2 or final_y == height // 2 else
            1 if left and top else
            2 if not left and top else
            3 if not left and not top else
            4
        )

        return final_x, final_y, quadrant


def get_robot_positions():
    with open('inputs/day14.txt') as f:
        return [line.strip() for line in f if line.strip()]


def parse_robot_positions(robot_positions):
    r = re.compile(r'p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)')
    return [Robot(*map(int, r.match(pos).groups())) for pos in robot_positions]


def part1(robots: list[Robot], width: int, height: int):
    final_positions = [robot.part1_position(100, width, height) for robot in robots]

    quadrant_counts = [0] * 5
    for _, _, q in final_positions:
        quadrant_counts[q] += 1

    return prod(quadrant_counts[1:])


def score_robots(positions, width, block_size=8):
    mid_x = width // 2

    reflected_positions = {(abs(mid_x - x), y) for x, y in positions}
    common_points = len(reflected_positions & positions)
    total_points = len(reflected_positions | positions)
    symmetry_score =  common_points / total_points if total_points else 0

    total_occupied_spaces = len(positions)
    blocks = Counter((x // block_size, y // block_size) for x, y in positions)

    entropy = 0
    for c in blocks.values():
        if c > 1:
            p = c / total_occupied_spaces
            entropy -= p * log2(p)

    return entropy - symmetry_score


def part2(robots: list[Robot], width: int, height: int, steps: int) -> int:
    best_time = -1
    best_score = float('inf')

    for t in range(steps):
        positions = {robot.position_at(t, width, height) for robot in robots}
        score = score_robots(positions, width)

        if score < best_score:
            best_score = score
            best_time = t

    return best_time


def main():
    robot_positions = get_robot_positions()
    robots = parse_robot_positions(robot_positions)
    print(f"Part 1: {part1(robots, 101, 103)}")
    print(f"Part 1: {part2(robots, 101, 103, 10000)}")