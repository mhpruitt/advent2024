import pytest
import day9

example_data = "2333133121414131402"

@pytest.fixture
def example_file_map():
    return day9.parse_file_map(example_data)

def test_day9_part1(example_file_map):
    blocks = day9.bad_defrag(example_file_map)
    assert day9.calculate_checksum(blocks) == 1928

def test_day9_part2(example_file_map):
    blocks = day9.confusing_defrag(example_file_map)
    assert day9.calculate_checksum(blocks) == 2858

