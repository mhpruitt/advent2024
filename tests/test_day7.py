import pytest
import day7

test_data = [
    (190, [10, 19], True),
    (3267, [81, 40, 27], True),
    (83, [17, 5], False),
    (156, [15, 6], False),
    (7290, [6, 8, 6, 15], False),
    (161011, [16, 10, 13], False),
    (192, [17, 8, 14], False),
    (21037, [9, 7, 18, 13], False),
    (292, [11, 6, 16, 20], True),
]

@pytest.mark.parametrize("total,values,possible", test_data)
def test_day7_solvable(total, values, possible):
    assert day7.solve_p1(total, values) == possible

def test_day7_part1():
    test_data_part1 = [(total, values) for total, values, possible in test_data]
    assert day7.calibration_results(day7.solve_p1, test_data_part1) == 3749

def test_day7_part2():
    test_data_part2 = [(total, values) for total, values, possible in test_data]
    assert day7.calibration_results(day7.solve_p2, test_data_part2) == 11387