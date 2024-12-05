import pytest
import day5

from collections import defaultdict

test_rules = """
    47|53
    97|13
    97|61
    97|47
    75|29
    61|13
    75|53
    29|13
    97|29
    53|29
    61|53
    97|53
    61|29
    47|13
    75|47
    97|75
    47|61
    75|61
    47|29
    75|13
    53|13
"""

test_updates = """
    75,47,61,53,29
    97,61,53,29,13
    75,29,13
    75,97,47,61,53
    61,13,29
    97,13,75,29,47
"""

@pytest.fixture
def rules():
    rules = defaultdict(list)
    for line in test_rules.splitlines():
        if line:
            r1, r2 = map(int, line.strip().split("|"))
            rules[r1].append(r2)

    return rules

@pytest.fixture
def updates():
    updates = []
    for line in test_updates.splitlines():
        if line:
            updates.append(list(map(int, line.strip().split(","))))

    return updates

def test_day5_part1(rules, updates):
    assert day5.part1(rules, updates) == 143

def test_day5_part2(rules, updates):
    assert day5.part2(rules, updates) == 123