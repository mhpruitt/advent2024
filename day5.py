"""
--- Day 5: Print Queue ---

https://adventofcode.com/2024/day/5
"""
from collections import defaultdict
from graphlib import TopologicalSorter

def build_page_rules():
    rules = defaultdict(set)
    with open("inputs/day5_rules.txt") as f:
        while line := f.readline().strip():
            r1, r2 = map(int, line.split('|'))
            rules[r1].add(r2)

    return rules

def get_updates():
    updates = []
    with open("inputs/day5_inputs.txt") as f:
        while line := f.readline().strip():
            updates.append(list(map(int, line.split(','))))

    return updates

def is_valid_update(rules, update):
    index_map = {page: i for i, page in enumerate(update)}
    return all(
        index_map[page] < index_map[must_follow]
        for page, pages_that_follow in rules.items()
        for must_follow in pages_that_follow
        if page in index_map and must_follow in index_map
    )

def find_middle_sum(updates):
    return sum([update[len(update) // 2] for update in updates])

def topo_sort(rules, update):
    ts = TopologicalSorter({k: rules[k] for k in update if k in rules.keys()})
    return [n for n in ts.static_order() if n in update]

def part1(rules, updates):
    return find_middle_sum([update for update in updates if is_valid_update(rules, update)])

def part2(rules, updates):
    corrected_updates = [topo_sort(rules, update) for update in updates if not is_valid_update(rules, update)]
    return find_middle_sum(corrected_updates)

def main():
    rules = build_page_rules()
    updates = get_updates()

    print(f"Part 1: {part1(rules, updates)}")
    print(f"Part 2: {part2(rules, updates)}")
