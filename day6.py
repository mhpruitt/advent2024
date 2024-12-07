"""
--- Day 6: Guard Gallivant  ---

https://adventofcode.com/2024/day/6
"""

def get_patrol_map():
    patrol_map = []

    with open('inputs/day6.txt') as f:
        while line := f.readline().strip():
            patrol_map.append(list(line))

    return patrol_map

def find_starting_position(patrol_map: list[list[str]]) -> tuple[int, int]:
    starting_row, starting_col = 0, 0

    for row, line in enumerate(patrol_map):
        if '^' in line:
            starting_col = line.index('^')
            starting_row = row
            break

    return starting_row, starting_col

def is_blocked_ahead(patrol_map: list[list[str]], current_position: tuple[int, int], direction: str) -> bool:
    row, col = current_position
    dr, dc = {'^': (-1,0), ">": (0,1), "v": (1,0), "<": (0,-1)}[direction]

    if row+dr < 0 or row+dr >= len(patrol_map):
        return False

    if col+dc < 0 or col+dc >= len(patrol_map[row]):
        return False

    cell_ahead = patrol_map[row+dr][col+dc]
    if cell_ahead == '#':
        return True

def turn_right(current_direction: str) -> str:
    return {'^': '>', '>': 'v', 'v': '<', '<': '^'}[current_direction]

def move_ahead(current_direction: str, current_position: tuple[int, int]) -> tuple[int, int]:
    row, col = current_position

    return {'^': (row-1,col), '>': (row,col+1), 'v': (row+1,col), '<': (row,col-1)}[current_direction]

import copy
def part1(patrol_map: list[list[str]], obstacle: tuple[int, int] | None = None):
    _patrol_map = copy.deepcopy(patrol_map)
    if obstacle:
        _patrol_map[obstacle[0]][obstacle[1]] = '#'

    current_pos = find_starting_position(_patrol_map)

    current_dir = '^'
    path = set()
    cycles = set()
    max_rows, max_cols = len(_patrol_map), len(_patrol_map[0])

    while 0 <= current_pos[0] < max_rows and 0 <= current_pos[1] < max_cols:
        path.add(current_pos)
        cycles.add((current_pos, current_dir))

        if is_blocked_ahead(_patrol_map, current_pos, current_dir):
            current_dir = turn_right(current_dir)
        else:
            current_pos = move_ahead(current_dir, current_pos)

        if obstacle and (current_pos, current_dir) in cycles:
            return -1

    return len(path)

def part2(patrol_map: list[list[str]]):
    starting_pos = find_starting_position(patrol_map)

    added_obstacles = set()
    for row in range(len(patrol_map)):
        for col in range(len(patrol_map[row])):
            if patrol_map[row][col] == '.' and (row, col) != starting_pos:
                if part1(patrol_map, obstacle=(row, col)) == -1:
                    added_obstacles.add((row, col))

    return len(added_obstacles)

def main():
    patrol_map = get_patrol_map()

    print(f'Part 1: {part1(patrol_map)}')
    print(f'Part 2: {part2(patrol_map)}')
