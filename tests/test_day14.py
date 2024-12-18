import pytest
import day14

example_positions = \
    """p=0,4 v=3,-3
       p=6,3 v=-1,-3
       p=10,3 v=-1,2
       p=2,0 v=2,-1
       p=0,0 v=1,3
       p=3,0 v=-2,-2
       p=7,6 v=-1,-3
       p=3,0 v=-1,-2
       p=9,3 v=2,3
       p=7,3 v=-1,2
       p=2,4 v=2,-3
       p=9,5 v=-3,-3""".splitlines()

example_robots = day14.parse_robot_positions([line.strip() for line in example_positions])

def test_day14_part1():
    assert day14.part1(example_robots, 11, 7) == 12