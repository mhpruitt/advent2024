"""
--- Day 15: Warehouse Woes ---

https://adventofcode.com/2024/day/15
"""

from abc import ABC, abstractmethod
from functools import singledispatchmethod
from dataclasses import dataclass
from enum import Enum
from typing import List, TypeVar, Generic

T = TypeVar("T")
W = TypeVar("W", bound="Warehouse")


class Direction(Enum):
    UP = ('^', -1, 0)
    DOWN = ('v', 1, 0)
    LEFT = ('<', 0, -1)
    RIGHT = ('>', 0, 1)

    @classmethod
    def from_char(cls, char: str) -> 'Direction':
        return next(d for d in cls if d.value[0] == char)


@dataclass
class Position:
    row: int
    col: int

    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        return (self.row, self.col) == (other.row, other.col)

    @singledispatchmethod
    def __add__(self, other: 'Position') -> 'Position':
        return Position(self.row + other.row, self.col + other.col)

    @__add__.register
    def _(self, other: Direction):
        dx, dy = other.value[1], other.value[2]
        return Position(self.row + dx, self.col + dy)


@dataclass
class BigBox:
    left: Position

    @property
    def right(self) -> Position:
        return Position(self.left.row, self.left.col + 1)

    def move(self, direction: Direction) -> 'BigBox':
        new_left = self.left + direction
        return BigBox(new_left)

    def __eq__(self, other):
        return self.left == other.left

    def __hash__(self):
        return hash(self.left)


@dataclass
class Warehouse(Generic[T], ABC):
    grid: list[list[str]]
    robot_pos: Position
    boxes: set[T]

    @classmethod
    @abstractmethod
    def from_input(cls: type[W], lines: List[str]) -> W:
        pass

    @abstractmethod
    def get_pushed_boxes(self, start_box: T, direction: Direction) -> list[T]:
        pass

    @abstractmethod
    def move_robot(self, direction: Direction) -> bool:
        pass

    def is_wall(self, pos: Position) -> bool:
        return self.grid[pos.row][pos.col] == '#'

    def can_move(self, pos: Position) -> bool:
        return not self.is_wall(pos)


@dataclass
class Part2Warehouse(Warehouse[BigBox]):
    @classmethod
    def from_input(cls, layout: list[str]) -> 'Part2Warehouse':
        # First, double the width of the layout
        wide_layout = []
        for line in layout:
            wide_line = ""
            robot_pos = None

            for c in line:
                match c:
                    case '#':
                        wide_line += '##'
                    case 'O':
                        wide_line += '[]'
                    case '.':
                        wide_line += '..'
                    case '@':
                        wide_line += '@.'

            wide_layout.append(wide_line)

        # Now process the wide layout
        grid = [list(line.strip()) for line in wide_layout]
        robot_pos = None
        boxes = set()

        for i, row in enumerate(grid):
            for j in range(0, len(row), 2):  # Step by 2 to handle wide boxes
                if j + 1 >= len(row):
                    continue

                if row[j] == '@':
                    robot_pos = Position(i, j)
                    grid[i][j] = '.'
                elif row[j] == '[' and row[j + 1] == ']':
                    boxes.add(BigBox(Position(i, j)))
                    grid[i][j] = '.'
                    grid[i][j + 1] = '.'

        return cls(grid, robot_pos, boxes)

    def get_box_at(self, pos: Position) -> BigBox | None:
        for box in self.boxes:
            if pos in (box.left, box.right):
                return box

        return None


    def get_pushed_boxes(self, start_box: BigBox, direction: Direction) -> list[BigBox]:
        boxes_to_push = {start_box}
        boxes_to_process = [start_box]

        while boxes_to_process:
            current_box = boxes_to_process.pop(0)
            moved_box = current_box.move(direction)

            # Check both positions of the moved box for contacts
            for check_pos in [moved_box.left, moved_box.right]:
                # Find any box that would be touched at this position
                touched_box = self.get_box_at(check_pos)
                if touched_box and touched_box not in boxes_to_push:
                    boxes_to_push.add(touched_box)
                    boxes_to_process.append(touched_box)

        return sorted(boxes_to_push, key=lambda box: (box.left.row, box.left.col))


    def move_robot(self, direction: Direction) -> None:
        new_pos = self.robot_pos + direction

        # Check if movement is blocked by wall
        if not self.can_move(new_pos):
            return

        # Check if we're moving into a box
        start_box = self.get_box_at(new_pos)
        if start_box is None:
            self.robot_pos = new_pos
            return

        # Get chain of boxes to push
        boxes_to_push = self.get_pushed_boxes(start_box, direction)

        # Check if all boxes can be moved to their new positions
        moved_positions = set()

        # First verify all moves are valid
        for box in boxes_to_push:
            new_box = box.move(direction)
            # Check if new position is valid
            if not self.can_move(new_box.left) or not self.can_move(new_box.right):
                return

            # Add positions to our tracking set
            moved_positions.add(new_box.left)
            moved_positions.add(new_box.right)

        # If positions overlap, movement is invalid
        if len(moved_positions) != 2 * len(boxes_to_push):
            return

        # All moves are valid, now perform them
        for box in boxes_to_push:
            self.boxes.remove(box)

        for box in boxes_to_push:
            self.boxes.add(box.move(direction))

        # Move robot
        self.robot_pos = new_pos


    def part2(self, moves: list[Direction]) -> int:
        for direction in moves:
            self.move_robot(direction)

        return sum(100 * pos.left.row + pos.left.col for pos in self.boxes)



@dataclass
class Part1Warehouse(Warehouse[Position]):

    @classmethod
    def from_input(cls, layout: list[str]) -> 'Part1Warehouse':
        grid = [list(line.strip()) for line in layout]
        robot_pos = None
        boxes = set()

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                match cell:
                    case '@':
                        robot_pos = Position(i, j)
                        grid[i][j] = '.'
                    case 'O':
                        boxes.add(Position(i, j))
                        grid[i][j] = '.'

        return cls(grid, robot_pos, boxes)


    def get_pushed_boxes(self, start_pos: Position, direction: Direction) -> list[Position]:
        boxes_to_push = [start_pos]

        current_pos = start_pos
        while True:
            next_pos = current_pos + direction

            if not self.can_move(next_pos):
                break

            if next_pos in self.boxes:
                boxes_to_push.append(next_pos)
                current_pos = next_pos
            else:
                break

        return boxes_to_push


    def move_robot(self, direction: Direction) -> None:
        new_pos = self.robot_pos + direction

        # Check if movement is blocked by wall
        if not self.can_move(new_pos):
            return

        # Get chain of boxes to push if there's a box
        boxes_to_push = []
        if new_pos in self.boxes:
            boxes_to_push = self.get_pushed_boxes(new_pos, direction)

        # If no boxes to push, just move robot
        if not boxes_to_push:
            self.robot_pos = new_pos
            return

        # Check if last box can be pushed
        last_box = boxes_to_push[-1]
        final_pos = last_box + direction

        if not self.can_move(final_pos):
            return

        # Move boxes
        self.boxes.remove(boxes_to_push[0])
        for i in range(len(boxes_to_push) - 1):
            self.boxes.remove(boxes_to_push[i + 1])
            self.boxes.add(boxes_to_push[i] + direction)
        self.boxes.add(final_pos)

        # Move robot
        self.robot_pos = new_pos


    def part1(self, moves: list[Direction]) -> int:
        """Calculate sum of GPS coordinates for all boxes"""
        for direction in moves:
            self.move_robot(direction)

        return sum(100 * pos.row + pos.col for pos in self.boxes)



def load_data():
    with open("inputs/day15_warehouse.txt") as w, open("inputs/day15_moves.txt") as m:
        return w.readlines(), m.readlines()


def parse_moves(all_moves):
    return [Direction.from_char(move) for line in all_moves for move in line.strip()]


def main():
    raw_warehouse, raw_moves = load_data()
    moves = parse_moves(raw_moves)

    warehouse_p1 = Part1Warehouse.from_input(raw_warehouse)
    warehouse_p2 = Part2Warehouse.from_input(raw_warehouse)

    print(f"Part 1: {warehouse_p1.part1(moves)}")
    print(f"Part 1: {warehouse_p2.part2(moves)}")
