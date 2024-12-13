import pytest
import day12

part1_plot1 = \
   """AAAA
      BBCD
      BBCC
      EEEC"""

part1_plot2 = \
   """OOOOO
      OXOXO
      OOOOO
      OXOXO
      OOOOO"""

part1_plot3 = \
   """RRRRIICCFF
      RRRRIICCCF
      VVRRRCCFFF
      VVRCCCJFFF
      VVVVCJJCFE
      VVIVCCJJEE
      VVIIICJJEE
      MIIIIIJJEE
      MIIISIJEEE
      MMMISSJEEE"""

part2_plot1 = \
    """AAAA
       BBCD
       BBCC
       EEEC"""

part2_plot2 = \
    """EEEEE
       EXXXX
       EEEEE
       EXXXX
       EEEEE"""

part2_plot3 = \
    """AAAAAA
       AAABBA
       AAABBA
       ABBAAA
       ABBAAA
       AAAAAA"""

def get_plot(request):
    lines = []
    for line in request.param[0].splitlines():
        lines.append(list(line.strip()))
    return lines, request.param[1]

@pytest.fixture(
    params=[
        (part1_plot1, 140),
        (part1_plot2, 772),
        (part1_plot3, 1930)
    ],
    ids=["p1_1", "p1_2", "p1_3"]
)
def part_one_plots(request):
    return get_plot(request)

@pytest.fixture(
    params=[
        (part2_plot1, 80),
        (part1_plot2, 436),
        (part2_plot2, 236),
        (part2_plot3, 368)
    ],
    ids=["p2_1", "p2_2", "p2_3", "p2_4"]
)
def part_two_plots(request):
    return get_plot(request)


def test_day12_part1(part_one_plots):
    plot, price = part_one_plots

    calculator = day12.GardenCalculator(plot)
    assert calculator.p1_price() == price

def test_day12_part2(part_two_plots):
    plot, price = part_two_plots

    calculator = day12.GardenCalculator(plot)
    assert calculator.p2_price() == price