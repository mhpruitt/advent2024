"""
--- Day 16: Reindeer Maze ---

https://adventofcode.com/2024/day/16
"""

import heapq
from dataclasses import dataclass
from enum import Enum
from typing import Iterator
from collections import defaultdict


type Position = tuple[int, int]
type PathNode = tuple[State, int]
type Maze = list[str]
type MazeDetails = tuple[list[State], float, set[Position]]


class Direction(Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    def turn_clockwise(self) -> 'Direction':
        return {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH
        }[self]

    def turn_counterclockwise(self) -> 'Direction':
        return {
            Direction.NORTH: Direction.WEST,
            Direction.EAST: Direction.NORTH,
            Direction.SOUTH: Direction.EAST,
            Direction.WEST: Direction.SOUTH
        }[self]


@dataclass(frozen=True)
class State:
    x: int
    y: int
    facing: Direction

    def move_forward(self) -> 'State':
        dx, dy = self.facing.value
        return State(self.x + dx, self.y + dy, self.facing)

    def get_neighbors(self, maze: list[str]) -> Iterator[PathNode]:
        # Try moving forward
        next_state = self.move_forward()
        if is_valid_position(next_state.x, next_state.y, maze):
            yield next_state, 1  # Cost of 1 for moving forward

        # Try turning clockwise/counterclockwise
        for new_dir in [self.facing.turn_clockwise(), self.facing.turn_counterclockwise()]:
            yield State(self.x, self.y, new_dir), 1000  # Cost of 1000 for turning

    def position_key(self) -> tuple[int, int]:
        return self.x, self.y

    def __lt__(self, other: 'State') -> bool:
        return self.x < other.x and self.y < other.y


def is_valid_position(x: int, y: int, maze: Maze) -> bool:
    if y < 0 or y >= len(maze) or x < 0 or x >= len(maze[0]):
        return False

    return maze[y][x] != '#'


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x2 - x1) + abs(y2 - y1)


def find_start_end(maze: Maze) -> tuple[Position, Position]:
    start = end = None
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)

    return start, end


def solve_maze(maze: Maze, sigma: float = 0.1) -> MazeDetails | None:
    start_pos, end_pos = find_start_end(maze)
    start_state = State(start_pos[0], start_pos[1], Direction.EAST)  # Initial state: at start position, facing east

    # Priority queue for Dijkstra - (distance, state)
    queue = [(0, start_state)]

    # Track distances and paths
    distances = defaultdict(lambda: float('inf'))
    distances[start_state] = 0
    came_from = {}

    # For each state, keep track of all predecessors that led to it optimally
    # This lets us reconstruct all optimal paths
    predecessors = defaultdict(set)

    while queue:
        current_dist, current_state = heapq.heappop(queue)

        # If we've found the end, we're done
        if (current_state.x, current_state.y) == end_pos:
            # Reconstruct path
            path = []
            state = current_state
            while state in came_from:
                path.append(state)
                state = came_from[state]

            path.append(start_state)
            path.reverse()

            # Second phase: Work backwards from end to find all tiles on optimal paths
            optimal_tiles = set()

            # Find all end states that achieved optimal score
            end_states = {state for state in distances
                          if state.position_key() == end_pos and
                          abs(distances[state] - current_dist) < sigma}

            # Stack for depth-first traversal of predecessor graph
            stack = list(end_states)
            visited_states = set()

            # Traverse backwards through all optimal predecessors
            while stack:
                current_state = stack.pop()

                if current_state in visited_states:
                    continue

                visited_states.add(current_state)
                optimal_tiles.add(current_state.position_key())

                # Add all predecessors that could lead to this state optimally
                for pred in predecessors[current_state]:
                    if distances[pred] + manhattan_distance(*pred.position_key(),
                                                            *current_state.position_key()) <= current_dist:
                        stack.append(pred)

            return path, current_dist, optimal_tiles

        # If we've found a worse path to this state, skip it
        if current_dist > distances[current_state]:
            continue

        # Explore neighbors
        for next_state, cost in current_state.get_neighbors(maze):
            distance = current_dist + cost

            # If this path to next_state is optimal (same as best known)
            if abs(distance - distances[next_state]) < sigma:
                predecessors[next_state].add(current_state)

            if distance < distances[next_state]:
                # Found a better path to this state
                distances[next_state] = distance
                predecessors[next_state] = {current_state}
                came_from[next_state] = current_state
                heapq.heappush(queue, (distance, next_state))

    return None


def load_maze() -> Maze:
    with open('inputs/day16.txt') as f:
        return f.readlines()


def main():
    _, path_cost, all_optimal_tiles = solve_maze(load_maze())

    print(f"Part 1: {path_cost}")
    print(f"Part 2: {len(all_optimal_tiles)}")