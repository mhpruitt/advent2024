import pytest
import day6

example_patrol_map = """
    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...
"""

@pytest.fixture
def example_map():
    lines = []
    for line in example_patrol_map.splitlines():
        if line:
            lines.append(list(line.strip()))

    return lines

def test_day6_part1(example_map):
    assert day6.part1(example_map) == 41

def test_day6_part2(example_map):
    assert day6.part2(example_map) == 6