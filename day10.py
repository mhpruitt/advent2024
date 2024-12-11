"""
--- Day 10: Hoof It ---

https://adventofcode.com/2024/day/10
"""

def load_trail_map():
    lines = []
    with open("inputs/day10.txt") as f:
        while line := f.readline():
            lines.append(list(map(int, line.strip())))

    return lines

def get_trailheads(topo_map):
    return [
        (i, j)
        for i in range(len(topo_map))
        for j in range(len(topo_map[0]))
        if topo_map[i][j] == 0
    ]

def hike_to_peak(topo_map, pos, path):
    x, y = pos
    current_height = topo_map[x][y]

    if current_height == 9:
        return {pos}, 1

    peaks, total = set(), 0
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = x + dx, y + dy
        next_pos = nx, ny
        if 0 <= nx < len(topo_map) and 0 <= ny < len(topo_map[0]) and next_pos not in path:
            if topo_map[nx][ny] == current_height+1:
                discovered_peaks, peak_count = hike_to_peak(topo_map, next_pos, path | {next_pos})
                peaks.update(discovered_peaks)
                total += peak_count

    return peaks, total

def trailhead_scores(topo_map):
    trailheads = get_trailheads(topo_map)
    return sum(len(hike_to_peak(topo_map, trailhead, {trailhead})[0]) for trailhead in trailheads)

def trailhead_ratings(topo_map):
    trailheads = get_trailheads(topo_map)
    return sum(hike_to_peak(topo_map, trailhead, {trailhead})[1] for trailhead in trailheads)

def main():
    topo_map = load_trail_map()
    print(f"Part 1: {trailhead_scores(topo_map)}")
    print(f"Part 2: {trailhead_ratings(topo_map)}")
