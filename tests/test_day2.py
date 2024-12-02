import pytest
import day2

test_data_part1 = [
    ([7, 6, 4, 2, 1], True),
    ([1, 3, 6, 7, 9], True),
    ([1, 2, 7, 8, 9], False),
    ([9, 7, 6, 2, 1], False),
    ([1, 3, 2, 4, 5], False),
    ([8, 6, 4, 4, 1], False),
]

test_data_part2 = [
    ([7, 6, 4, 2, 1], True),
    ([1, 3, 6, 7, 9], True),
    ([1, 2, 7, 8, 9], False),
    ([9, 7, 6, 2, 1], False),
    ([1, 3, 2, 4, 5], True),
    ([8, 6, 4, 4, 1], True),
    ([27, 29, 32, 33, 36, 37, 40, 37], True),
    ([71, 74, 77, 80, 83, 80, 83], False)
]

@pytest.mark.parametrize("data,expected", test_data_part1)
def test_day2_part1(data, expected):
    assert day2.check_if_all_safe(data) == expected

@pytest.mark.parametrize("data,expected", test_data_part2)
def test_day2_part2(data, expected):
    assert day2.check_if_all_safe_with_damper(data) == expected