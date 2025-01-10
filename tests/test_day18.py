import pytest
import day18

example = \
    """
    5,4
    4,2
    4,5
    3,0
    2,1
    6,3
    2,4
    1,5
    0,6
    3,3
    2,6
    5,1
    1,2
    5,5
    2,5
    6,5
    1,4
    0,4
    6,4
    1,1
    6,1
    1,0
    0,5
    1,6
    2,0
    """

@pytest.fixture
def example_part1():
    return day18.parse_input(example.strip().splitlines()), 6, 12, 22


@pytest.fixture
def example_part2():
    return day18.parse_input(example.strip().splitlines()), 6, 12, (6,1)


def test_part1(example_part1):
    corrupted_memory, size, limit, steps = example_part1

    assert day18.bfs(corrupted_memory, size, limit) == steps


def test_part2(example_part2):
    corrupted_memory, size, known_possible, blocking_coord = example_part2

    assert day18.blocking_coord(corrupted_memory, size, known_possible) == blocking_coord
