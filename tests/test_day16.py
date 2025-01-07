import pytest
import day16

test_maze_1 = \
    """###############
       #.......#....E#
       #.#.###.#.###.#
       #.....#.#...#.#
       #.###.#####.#.#
       #.#.#.......#.#
       #.#.#####.###.#
       #...........#.#
       ###.#.#####.#.#
       #...#.....#.#.#
       #.#.#.###.#.#.#
       #.....#...#.#.#
       #.###.#.#.#.#.#
       #S..#.....#...#
       ###############"""

test_maze_2 = \
    """#################
       #...#...#...#..E#
       #.#.#.#.#.#.#.#.#
       #.#.#.#...#...#.#
       #.#.#.#.###.#.#.#
       #...#.#.#.....#.#
       #.#.#.#.#.#####.#
       #.#...#.#.#.....#
       #.#.#####.#.###.#
       #.#.#.......#...#
       #.#.###.#####.###
       #.#.#...#.....#.#
       #.#.#.#####.###.#
       #.#.#.........#.#
       #.#.#.#########.#
       #S#.............#
       #################"""

@pytest.fixture(
    params=[
        (test_maze_1, 7036),
        (test_maze_2, 11048)
    ],
    ids=['p1_1', 'p1_2']
)
def example_part1_maze(request):
    return [line.strip() for line in request.param[0].splitlines()], request.param[1]

@pytest.fixture(
    params=[
        (test_maze_2, 64)
    ],
    ids=['p2_1']
)
def example_part2_maze(request):
    return [line.strip() for line in request.param[0].splitlines()], request.param[1]


def test_day16_part1(example_part1_maze):
    maze, path_cost = example_part1_maze
    _, cost, _ = day16.solve_maze(maze)

    assert cost == path_cost

def test_day16_part2(example_part2_maze):
    maze, optimal_tile_count = example_part2_maze
    _, _, optimal_tiles = day16.solve_maze(maze)

    assert len(optimal_tiles) == optimal_tile_count