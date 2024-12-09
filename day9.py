"""
--- Day 9: Disk Fragmenter ---

https://adventofcode.com/2024/day/9
"""
from collections import deque
from copy import deepcopy

def load_file_map():
    with open("inputs/day9.txt") as f:
        return f.readline().strip()

def parse_file_map(file_map):
    blocks = []
    file_id = 0

    for i in range(0, len(file_map)-1, 2):
        file_size, free_size = map(int, file_map[i:i + 2])
        blocks.extend([file_id] * file_size)  # File blocks
        blocks.extend(['.'] * free_size)
        file_id += 1

    if len(file_map) % 2 == 1:
        blocks.extend([file_id] * int(file_map[-1]))

    return blocks

def calculate_checksum(blocks):
    return sum(idx * int(block) for idx, block in enumerate(blocks) if block != '.')

def bad_defrag(blocks):
    n = len(blocks)
    free_blocks = deque(idx for idx, block in enumerate(blocks) if block == '.')

    for i in range(n - 1, -1, -1):
        if blocks[i] != '.' and free_blocks and free_blocks[0] < i:
            free_index = free_blocks.popleft()
            blocks[free_index], blocks[i] = blocks[i], '.'
            free_blocks.append(i)

    return blocks


def confusing_defrag(blocks):
    max_file_id = max(block for block in blocks if block != '.')
    for current_id in range(max_file_id, -1, -1):
        file_start = blocks.index(current_id)
        file_size = 0
        for i in range(file_start, len(blocks)):
            if blocks[i] == current_id:
                file_size += 1
            else:
                break

        best_pos = -1
        space_count = 0
        for i in range(len(blocks)):
            if blocks[i] == '.':
                space_count += 1
                if space_count >= file_size:
                    best_pos = i - file_size + 1
                    break
            else:
                space_count = 0

        if best_pos != -1 and best_pos < file_start:
            for i in range(file_start, file_start + file_size):
                blocks[i] = '.'

            for i in range(best_pos, best_pos + file_size):
                blocks[i] = current_id

        print(current_id)

    return blocks

def main():
    file_map = load_file_map()
    blocks = parse_file_map(file_map)

    print("Part 1:", calculate_checksum(bad_defrag(deepcopy(blocks))))
    print("Part 2:", calculate_checksum(confusing_defrag(deepcopy(blocks))))