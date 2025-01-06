import pytest
import day15

raw_part1_small_warehouse_example = \
    """########
       #..O.O.#
       ##@.O..#
       #...O..#
       #.#.O..#
       #...O..#
       #......#
       ########"""

raw_part1_small_moves_example = "<^^>>>vv<v>>v<<"

raw_large_warehouse_example = \
    """##########
       #..O..O.O#
       #......O.#
       #.OO..O.O#
       #..O@..O.#
       #O#..O...#
       #O..O..O.#
       #.OO.O.OO#
       #....O...#
       ##########"""

raw_large_moves_example = \
    """<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
       vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
       ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
       <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
       ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
       ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
       >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
       <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
       ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
       v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

raw_part2_warehouse_example = \
    """####################
       ##....[]....[]..[]##
       ##............[]..##
       ##..[][]....[]..[]##
       ##....[]@.....[]..##
       ##[]##....[]......##
       ##[]....[]....[]..##
       ##..[][]..[]..[][]##
       ##........[]......##
       ####################"""


@pytest.fixture(
    params=[
        (raw_part1_small_warehouse_example, raw_part1_small_moves_example, 2028),
        (raw_large_warehouse_example, raw_large_moves_example, 10092)
    ],
    ids=['p1_small', 'p1_large']
)
def example_part1_warehouses(request):
    return (
        day15.Part1Warehouse.from_input(request.param[0].splitlines()),
        day15.parse_moves(request.param[1].splitlines()),
        request.param[2]
    )

@pytest.fixture(
    params=[
        (raw_large_warehouse_example, raw_large_moves_example, 9021)
    ],
    ids=['p2_large']
)
def example_part2_warehouses(request):
    return (
        day15.Part2Warehouse.from_input(request.param[0].splitlines()),
        day15.parse_moves(request.param[1].splitlines()),
        request.param[2]
    )


def test_day15_part1(example_part1_warehouses):
    warehouse, moves, score = example_part1_warehouses
    assert warehouse.part1(moves) == score

def test_day15_part2(example_part2_warehouses):
    warehouse, moves, score = example_part2_warehouses
    assert warehouse.part2(moves) == score