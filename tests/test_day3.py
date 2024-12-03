import day3

def test_day3_part1():
    assert day3.sum_multiplications(r"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))") == 161

def test_day2_part2():
    assert day3.conditionally_sum_multiplications(r"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))") == 48