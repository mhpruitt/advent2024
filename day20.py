from dataclasses import dataclass
from collections import deque


@dataclass(frozen=True)
class Point:
    __slots__ = ('x', 'y')
    x: int
    y: int

    def dist(self, other: 'Point') -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)


class RaceTrack:
    def __init__(self, grid: list[str]):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.start = self._find_char('S')
        self.end = self._find_char('E')
        self.base_path = self._find_base_path()


    def _find_char(self, char: str) -> Point:
        return next(
            Point(x, y)
            for y, row in enumerate(self.grid)
            for x, c in enumerate(row)
            if c == char
        )


    def is_wall(self, p: Point) -> bool:
        return not (0 <= p.x < self.width and 0 <= p.y < self.height) or self.grid[p.y][p.x] == '#'


    def neighbors(self, p: Point) -> list[Point]:
        return [
            Point(p.x + dx, p.y + dy)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]
            if not self.is_wall(Point(p.x + dx, p.y + dy))
        ]


    def _find_base_path(self) -> list[Point]:
        queue = deque([(self.start, [self.start])])
        seen = {self.start}

        while queue:
            pos, path = queue.popleft()
            if pos == self.end:
                return path

            for next_pos in self.neighbors(pos):
                if next_pos not in seen:
                    seen.add(next_pos)
                    queue.append((next_pos, path + [next_pos]))

        raise ValueError("No path found")


    def find_cheats(self, max_dist: int = 2) -> list[int]:
        savings = []

        for i, p1 in enumerate(self.base_path):
            for j in range(i + 3, len(self.base_path)):
                p2 = self.base_path[j]
                dist = p1.dist(p2)
                if dist <= max_dist and (j - i) > dist:
                    savings.append((j - i) - dist)

        return savings


def solve(track: RaceTrack, cheat_length: int, min_savings: int = 100) -> int:
    cheats = track.find_cheats(cheat_length)
    return sum(1 for saved in cheats if saved >= min_savings)


def load_input() -> str:
    with open("inputs/day20.txt") as f:
        return f.read()


def parse_input(problem_input: str) -> RaceTrack:
    lines = [line.strip() for line in problem_input.splitlines()]
    return RaceTrack(lines)


def main():
    track = parse_input(load_input())
    print(f'Part 1: {solve(track, 2)}')
    print(f'Part 2: {solve(track, 20)}')
