"""
--- Day 1: Historian Hysteria ---

https://adventofcode.com/2024/day/1
"""

def extract_lists():
    l1 = []
    l2 = []

    with open('inputs/day1.txt', 'r') as f:
        while nums := f.readline().strip().split():
            l1.append(int(nums[0]))
            l2.append(int(nums[1]))

    return l1, l2


def part1(l1: list, l2: list):
    l1.sort()
    l2.sort()

    cumulative_diff = sum([abs(e1-e2) for e1, e2 in zip(l1, l2)])
    return cumulative_diff


def part2(l1: list, l2: list):
    from collections import Counter

    counted_list_2 = Counter(l2)

    return sum([i*counted_list_2[i] for i in l1])

def main():
    list_1, list_2 = extract_lists()

    print(f'Part 1: {part1(list_1, list_2)}')
    print(f'Part 2: {part2(list_1, list_2)}')
