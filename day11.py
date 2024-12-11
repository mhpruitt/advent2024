"""
--- Day 11: Plutonian Pebbles ---

https://adventofcode.com/2024/day/11
"""

from collections import defaultdict


def get_stones():
    with open('inputs/day11.txt') as f:
        return list(map(int, f.readline().strip().split()))


def transform_stone(stone):
    if stone == 0:
        return [1]

    digits = str(stone)
    if len(digits) % 2 == 0:
        mid = len(digits) // 2
        left = int(digits[:mid])
        right = int(digits[mid:])
        return [left, right]

    return [stone * 2024]


class StoneEvolutionSimulator:
    def __init__(self, initial_stones):
        self.unique_stone_counts = defaultdict(int)
        for stone in initial_stones:
            self.unique_stone_counts[stone] += 1

    def step(self) -> None:
        new_counts = defaultdict(int)

        for stone, count in self.unique_stone_counts.items():
            for next_stone in transform_stone(stone):
                new_counts[next_stone] += count

        self.unique_stone_counts = new_counts

    def simulate(self, steps):
        for _ in range(steps):
            self.step()

        return sum(self.unique_stone_counts.values())

def main():
    stones = get_stones()

    print(f"Part 1: {StoneEvolutionSimulator(stones).simulate(25)}")
    print(f"Part 2: {StoneEvolutionSimulator(stones).simulate(75)}")