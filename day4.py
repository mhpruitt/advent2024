"""
--- Day 4: Ceres Search ---

https://adventofcode.com/2024/day/4
"""

def get_word_search():
    lines = []
    with open("inputs/day4.txt") as f:
        while line := f.readline().strip():
            lines.append(list(line))
    return lines

# Part 1
def part1(lines: list[list[str]]):
    word = 'XMAS'
    rows, cols = len(lines), len(lines[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    found_positions = []

    def dfs(r, dr, c, dc, idx, path):
        if idx == len(word):  # Word found
            found_positions.append(path[:])
            return
        if r < 0 or r >= rows or c < 0 or c >= cols or lines[r][c] != word[idx]:
            return

        path.append((r, c))
        dfs(r+dr, dr, c+dc, dc, idx + 1, path)
        path.pop()

    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == word[0]:
                for dr, dc in directions:
                    dfs(r, dr, c, dc, 0, [])

    return len(found_positions)

# Part 2
def part2(lines: list[list[str]]):
    rows, cols = len(lines), len(lines[0])
    combinations = [
        [(-1, -1, 'M'), (-1, 1, 'M'), (1, -1, 'S'), (1, 1, 'S')],
        [(-1, -1, 'S'), (-1, 1, 'M'), (1, -1, 'S'), (1, 1, 'M')],
        [(-1, -1, 'M'), (-1, 1, 'S'), (1, -1, 'M'), (1, 1, 'S')],
        [(-1, -1, 'S'), (-1, 1, 'S'), (1, -1, 'M'), (1, 1, 'M')],
    ]

    matches = 0
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            if lines[r][c] == 'A':
                if any(all(lines[r+dr][c+dc] == l for dr, dc, l in cm) for cm in combinations):
                    matches += 1

    return matches


def main():
    word_search = get_word_search()
    print(f'Part 1: {part1(word_search)}')
    print(f'Part 1: {part2(word_search)}')