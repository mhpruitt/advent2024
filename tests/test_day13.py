import pytest
import day13

example_equations = \
    """Button A: X+94, Y+34
       Button B: X+22, Y+67
       Prize: X=8400, Y=5400
       
       Button A: X+26, Y+66
       Button B: X+67, Y+21
       Prize: X=12748, Y=12176
       
       Button A: X+17, Y+86
       Button B: X+84, Y+37
       Prize: X=7870, Y=6450
       
       Button A: X+69, Y+23
       Button B: X+27, Y+71
       Prize: X=18641, Y=10279""".splitlines()

example_solutions_p1 = [280, None, 200, None]
example_machines_p1 = day13.parse_claw_machines(example_equations)


example_solutions_p2 = [False, True, False, True]
example_machines_p2 = day13.parse_claw_machines(example_equations, offset=10000000000000)


@pytest.mark.parametrize("machine_and_solution", zip(example_machines_p1, example_solutions_p1))
def test_day13_part1_individual(machine_and_solution: day13.ClawMachine):
    machine, solution = machine_and_solution
    a_presses, b_presses, tokens = machine.find_minimal_solution()

    assert tokens == solution

def test_day13_part1():
    total_tokens = sum([solution for solution in example_solutions_p1 if solution])
    assert day13.calc_total_tokens(example_machines_p1) == total_tokens

@pytest.mark.parametrize("machine_and_solution", zip(example_machines_p2, example_solutions_p2))
def test_day13_part2_individual(machine_and_solution: day13.ClawMachine):
    machine, solution = machine_and_solution
    a_presses, b_presses, tokens = machine.find_minimal_solution()

    assert solution == (tokens is not None)