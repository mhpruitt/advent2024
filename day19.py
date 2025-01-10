def load_input() -> str:
    with open("inputs/day19.txt") as f:
        return f.read()


def parse_input(problem_input: str) -> tuple[set[str], list[str]]:
    patterns, designs = problem_input.strip().split("\n\n")

    parsed_patterns = {p.strip() for p in patterns.split(',')}
    parsed_designs = [d.strip() for d in designs.splitlines()]

    return parsed_patterns, parsed_designs


def count_arrangements(patterns: set[str], target: str) -> int:
    dp = [0] * (len(target) + 1)
    dp[0] = 1  # Empty string can be constructed in one way

    for i in range(len(target) + 1):
        for pattern in patterns:
            if i + len(pattern) <= len(target) and target[i:i + len(pattern)] == pattern:
                dp[i + len(pattern)] += dp[i]

    return dp[len(target)]

def part1(patterns: set[str], designs: list[str]) -> int:
    return sum(1 for design in designs if count_arrangements(patterns, design) > 0)

def part2(patterns: set[str], designs: list[str]) -> int:
    return sum(count_arrangements(patterns, design) for design in designs)


def main():
    patterns, designs = parse_input(load_input())
    print(f'Part 1: {part1(patterns, designs)}')
    print(f'Part 2: {part2(patterns, designs)}')