import pytest
import day10

example_data = \
    """89010123
       78121874
       87430965
       96549874
       45678903
       32019012
       01329801
       10456732"""

@pytest.fixture
def example_topo_map():
    lines = []
    example_map = example_data.splitlines()
    for line in example_map:
        lines.append(list(map(int, line.strip())))

    return lines

def test_day10_part1(example_topo_map):
    assert day10.trailhead_scores(example_topo_map) == 36

def test_day10_part2(example_topo_map):
    assert day10.trailhead_ratings(example_topo_map) == 81

