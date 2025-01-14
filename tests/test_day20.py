import pytest
import day20

from collections import defaultdict

example = \
    """###############
       #...#...#.....#
       #.#.#.#.#.###.#
       #S#...#.#.#...#
       #######.#.#.###
       #######.#.#...#
       #######.#.###.#
       ###..E#...#...#
       ###.#######.###
       #...###...#...#
       #.#####.#.###.#
       #.#...#.#.#...#
       #.#.#.#.#.#.###
       #...#...#...###
       ###############"""


@pytest.fixture
def day20_example():
    return day20.parse_input(example)


def test_part1(day20_example):
    cheats = day20_example.find_cheats(2)

    savings_count = defaultdict(int)
    for saved in cheats:
        savings_count[saved] += 1

    assert savings_count[2] == 14
    assert savings_count[4] == 14
    assert savings_count[6] == 2
    assert savings_count[8] == 4
    assert savings_count[10] == 2
    assert savings_count[12] == 3
    assert savings_count[20] == 1
    assert savings_count[36] == 1
    assert savings_count[38] == 1
    assert savings_count[40] == 1
    assert savings_count[64] == 1

def test_part2(day20_example):
    cheats = day20_example.find_cheats(20)

    savings_count = defaultdict(int)
    for saved in cheats:
        savings_count[saved] += 1

    assert savings_count[50] == 32
    assert savings_count[52] == 31
    assert savings_count[54] == 29
    assert savings_count[56] == 39
    assert savings_count[58] == 25
    assert savings_count[60] == 23
    assert savings_count[62] == 20
    assert savings_count[64] == 19
    assert savings_count[66] == 12
    assert savings_count[68] == 14
    assert savings_count[70] == 12
    assert savings_count[72] == 22
    assert savings_count[74] == 4
    assert savings_count[76] == 3