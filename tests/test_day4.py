import day4

test_data = [
    list("MMMSXXMASM"),
    list("MSAMXMSMSA"),
    list("AMXSXMAAMM"),
    list("MSAMASMSMX"),
    list("XMASAMXAMM"),
    list("XXAMMXXAMA"),
    list("SMSMSASXSS"),
    list("SAXAMASAAA"),
    list("MAMMMXMMMM"),
    list("MXMXAXMASX"),
]

def test_day4_part1():
    assert day4.part1(test_data) == 18

def test_day4_part2():
    assert day4.part2(test_data) == 9