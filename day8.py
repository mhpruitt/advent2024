"""
--- Day 7: Day 8: Resonant Collinearity ---

https://adventofcode.com/2024/day/8
"""

from collections import defaultdict

def read_map():
    antenna_positions = defaultdict(list)

    with open("inputs/day8.txt") as f:
        map_data = f.readlines()
        rows, cols = len(map_data), len(map_data[0].strip())

        for r, row in enumerate(map_data):
            for c, col in enumerate(row.strip()):
                if col.isalnum():
                    antenna_positions[col].append((r, c))

        return rows, cols, antenna_positions


def compute_antinodes(p1, p2, rows, cols, max_nodes=1):
    dx, dy = p2[0]-p1[0], p2[1]-p1[1]
    antinodes = set()

    def in_bounds(point):
        x, y = point
        return 0 <= x < rows and 0 <= y < cols

    def project(point, direction):
        x, y = point
        return x + dx * direction, y + dy * direction

    for direction in (-1, 1):
        current_antinode = project(p1 if direction == -1 else p2, direction)
        for _ in range(max_nodes):
            if not in_bounds(current_antinode):
                break

            antinodes.add(current_antinode)
            current_antinode = project(current_antinode, direction)

    return antinodes

def count_antinodes(rows: int, cols: int, antennas, add_self=False, max_projections=1) -> int:
    antinodes = set()

    for freq, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                antinodes.update(compute_antinodes(positions[i], positions[j], rows, cols, max_projections))

        if add_self:
            antinodes.update(positions)

    return len(antinodes)


def main():
    rows, cols, antenna_positions = read_map()
    print(f"Part 1: {count_antinodes(rows, cols, antenna_positions)}")
    print(f"Part 1: {count_antinodes(rows, cols, antenna_positions, add_self=True, max_projections=max(rows, cols))}")