import pytest
import day11

example_data = [
    ([125, 17], 6, 22),
    ([125, 17], 25, 55312)
]

@pytest.mark.parametrize("initial,steps,count", example_data)
def test_day10(initial, steps, count):
    assert day11.StoneEvolutionSimulator(initial).simulate(steps) == count

