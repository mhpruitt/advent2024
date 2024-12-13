"""
--- Day 12: Garden Groups ---

https://adventofcode.com/2024/day/12
"""

from dataclasses import dataclass
from enum import Enum


class _D(Enum):
    """Enum for cardinal and intercardinal directions"""
    N = (-1, 0)
    S = (1, 0)
    E = (0, 1)
    W = (0, -1)
    NE = (-1, 1)
    SE = (1, 1)
    SW = (1, -1)
    NW = (-1, -1)


@dataclass
class Point:
    """Represents a point in the garden"""
    row: int
    col: int

    def __hash__(self) -> int:
        return hash((self.row, self.col))

class UnionFind:
    """Union-Find data structure with path compression and union by rank."""

    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False

        # Union by rank for balanced trees
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


class Region:
    """Represents a connected region of similar plants in the garden."""

    def __init__(self, plant_type: str):
        self.plant_type = plant_type
        self.points: set[Point] = set()
        self.area = 0
        self.perimeter = 0
        self.corner_count = 0

    def add_point(self, point: Point) -> None:
        self.points.add(point)
        self.area = len(self.points)


class GardenCalculator:
    """Calculates prices for garden fencing based on connected regions of plants."""

    def __init__(self, garden_map: list[list[str]]):
        self.garden = garden_map
        self.rows = len(garden_map)
        self.cols = len(garden_map[0])

        self.regions = self._identify_regions()
        self._calculate_corners()
        self._calculate_perimeters()

    def _identify_regions(self) -> dict[int, Region]:
        """Identifies connected regions using Union-Find"""
        uf = UnionFind(self.rows * self.cols)

        # Connect adjacent similar plants
        for r in range(self.rows):
            for c in range(self.cols):
                curr_idx = r * self.cols + c
                curr_plant = self.garden[r][c]

                # Only need to check right and down for connectivity
                for dr, dc in [(0, 1), (1, 0)]:
                    new_r, new_c = r + dr, c + dc
                    if self._is_valid_cell(new_r, new_c) and self.garden[new_r][new_c] == curr_plant:
                        uf.union(curr_idx, new_r * self.cols + new_c)

        # Build regions from Union-Find results
        regions: dict[int, Region] = {}
        for r in range(self.rows):
            for c in range(self.cols):
                curr_idx = r * self.cols + c
                root = uf.find(curr_idx)

                if root not in regions:
                    regions[root] = Region(self.garden[r][c])
                regions[root].add_point(Point(r, c))

        return regions

    def _is_valid_cell(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

    def _get_cell_value(self, point: Point) -> str:
        """Returns cell value or '#' for out of bounds"""
        if not self._is_valid_cell(point.row, point.col):
            return '#'

        return self.garden[point.row][point.col]

    def _calculate_perimeters(self) -> None:
        """Calculates perimeter for each region"""
        for region in self.regions.values():
            perimeter = 0
            for point in region.points:
                # Count edges adjacent to different plants or boundaries
                adjacent_sides = 4
                for dr, dc in _D.N.value, _D.S.value, _D.E.value, _D.W.value:
                    adj_point = Point(point.row + dr, point.col + dc)
                    if self._get_cell_value(adj_point) == region.plant_type:
                        adjacent_sides -= 1

                perimeter += adjacent_sides

            region.perimeter = perimeter

    def _calculate_corners(self) -> None:
        """Calculates corner count for each region"""
        for region in self.regions.values():
            corner_count = 0
            for point in region.points:
                neighbors = {
                    d: Point(point.row + d.value[0], point.col + d.value[1]) for d in _D
                }

                # Count 90° corners (two adjacent different neighbors)
                for dirs in [(_D.N, _D.E), (_D.E, _D.S), (_D.S, _D.W), (_D.W, _D.N)]:
                    if (self._get_cell_value(neighbors[dirs[0]]) != region.plant_type and
                        self._get_cell_value(neighbors[dirs[1]]) != region.plant_type):
                        corner_count += 1

                # Count 270° corners (two similar neighbors with different diagonal)
                for dirs in [(_D.N, _D.E, _D.NE), (_D.E, _D.S, _D.SE),
                             (_D.S, _D.W, _D.SW), (_D.W, _D.N, _D.NW)]:
                    if (self._get_cell_value(neighbors[dirs[0]]) == region.plant_type and
                        self._get_cell_value(neighbors[dirs[1]]) == region.plant_type and
                        self._get_cell_value(neighbors[dirs[2]]) != region.plant_type):
                        corner_count += 1

            region.corner_count = corner_count

    def p1_price(self):
        return sum(r.area * r.perimeter for r in self.regions.values())

    def p2_price(self):
        return sum(r.area * r.corner_count for r in self.regions.values())


def get_plot():
    lines = []
    with open("inputs/day12.txt") as f:
        while line := f.readline().strip():
            lines.append(list(line))

    return lines


def main():
    plot = get_plot()
    print(f"Part 1: {GardenCalculator(plot).p1_price()}")
    print(f"Part 2: {GardenCalculator(plot).p2_price()}")
