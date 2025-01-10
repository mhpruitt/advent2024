import pytest
import day19

example = \
    """r, wr, b, g, bwu, rb, gb, br

       brwrr
       bggr
       gbbr
       rrbgbr
       ubwu
       bwurrg
       brgr
       bbrgwb"""


@pytest.fixture
def example_part1():
    return day19.parse_input(example), 6

@pytest.fixture
def example_part2():
    return day19.parse_input(example), 16


def test_part1(example_part1):
    example_data, expected_designs = example_part1
    patterns, designs = example_data

    assert day19.part1(patterns, designs) == expected_designs


def test_part2(example_part2):
    example_data, arrangement_count = example_part2
    patterns, designs = example_data

    assert day19.part2(patterns, designs) == arrangement_count