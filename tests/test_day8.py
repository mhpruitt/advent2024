import pytest
import day8
from collections import defaultdict

example_data = \
    """......#....#
       ...#....0...
       ....#0....#.
       ..#....0....
       ....0....#..
       .#....A.....
       ...#........
       #......#....
       ........A...
       .........A..
       ..........#.
       ..........#."""

@pytest.fixture
def example_antenna_positions():
    antenna_positions = defaultdict(list)
    map_data = example_data.splitlines()
    rows, cols = len(map_data), len(map_data[0])

    for r, row in enumerate(map_data):
        for c, col in enumerate(row.strip()):
            if col.isalnum():
                antenna_positions[col].append((r, c))

    return rows, cols, antenna_positions


def test_day8_part1(example_antenna_positions):
    rows, cols, antenna_positions = example_antenna_positions
    assert day8.count_antinodes(rows, cols, antenna_positions) == 14

def test_day8_part2(example_antenna_positions):
    rows, cols, antenna_positions = example_antenna_positions
    assert day8.count_antinodes(rows, cols, antenna_positions, add_self=True, max_projections=max(rows, cols)) == 34