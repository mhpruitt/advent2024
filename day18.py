from collections import deque

type MemoryCoordinate = tuple[int, ...]

def load_input() -> list[str]:
    with open("inputs/day18.txt") as f:
        return f.readlines()


def parse_input(problem_input: list[str]) -> list[MemoryCoordinate]:
    return [tuple(map(int, line.strip().split(','))) for line in problem_input]


def bfs(corrupted_memory: list[MemoryCoordinate], size: int, limit: int) -> int | None:
    corrupted = {(x, y) for x, y in corrupted_memory[:limit]}
    queue = deque([(0, 0, 0)])
    visited = {(0, 0)}

    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == (size, size):
            return steps

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= size and 0 <= ny <= size and \
                    (nx, ny) not in visited and \
                    (nx, ny) not in corrupted:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return None

def blocking_coord(corrupted_memory: list[MemoryCoordinate], size: int, known_possible: int) -> MemoryCoordinate:
    left, right = known_possible, len(corrupted_memory) - 1
    while left < right:
        mid = (left + right) >> 1
        if bfs(corrupted_memory, size, mid + 1):
            left = mid + 1
        else:
            right = mid

    return corrupted_memory[left]

def main():
    size = 70
    limit = 1024
    corrupted_memory = parse_input(load_input())
    print(f'Part 1: {bfs(corrupted_memory, size, limit)}')
    print(f'Part 2: {blocking_coord(corrupted_memory, size, limit)}')
