"""
--- Day 4: Ceres Search ---

"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it.
After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if
you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words.
It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them.
Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not
involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

Take a look at the little Elf's word search. How many times does XMAS appear?

--- Part Two ---

The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an
X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S

Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written
forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an
X-MAS appear?


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