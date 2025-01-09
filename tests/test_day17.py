import pytest
import day17

part1_example = \
    """
    Register A: 729
    Register B: 0
    Register C: 0
    
    Program: 0,1,5,4,3,0
    """

part2_example = \
    """
    Register A: 17323786
    Register B: 0
    Register C: 0
    
    Program: 2,4,1,1,7,5,1,5,4,1,5,5,0,3,3,0
    """


@pytest.fixture
def example_part1(request):
    return day17.parse_input(part1_example.strip().splitlines()), [4,6,3,5,6,3,5,2,1,0]


@pytest.fixture
def example_part2(request):
    return day17.parse_input(part2_example.strip().splitlines()), 117440


def test_day17_part1(example_part1):
    program_details, output = example_part1
    a, b, c, program = program_details

    assert day17.Computer(a, b, c).run(program) == output
    
    
def test_day17_part2(example_part2):
    program_details, known_a  = example_part2
    a, b, c, program = program_details

    calculated_a = day17.find_self_replicating_a(program)
    assert day17.Computer(calculated_a, b, c).run(program) == program