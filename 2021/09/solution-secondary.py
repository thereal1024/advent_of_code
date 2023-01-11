#!/usr/bin/env python3

OFFSETS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

def valid_offsets(y, x, h, w):
    points = ((y+dy, x+dx) for dy, dx in OFFSETS)
    valid_points = ((y, x) for y, x in points if y in range(h) and x in range(w))
    return valid_points
    
def parse_map(lines):
    grid = []
    for line in lines:
        parsed = []
        for c in line:
            parsed.append(int(c))
        grid.append(parsed)
    return grid

def find_low_points(grid):
    h = len(grid)
    w = len(grid[0])
    
    low_points = []
    for y in range(h):
        for x in range(w):
            adj = valid_offsets(y, x, h, w)
            if all(grid[y][x] < grid[ay][ax] for ay, ax in adj):
                low_points.append((y, x))
    return low_points

def basin_area(grid, point):
    h = len(grid)
    w = len(grid[0])
    
    basin_points = set()
    to_scan = set([point])
    while len(to_scan) > 0:
        next_scan = set()
        for pt in to_scan:
            y, x = pt
            if grid[y][x] < 9:
                basin_points.add(pt)
                newpoints = set(valid_offsets(y, x, h, w)) - basin_points
                next_scan |= newpoints
        to_scan = next_scan
    
    return len(basin_points)

def solution(lines):
    grid = parse_map(lines)
    low_points = find_low_points(grid)
    basins = [basin_area(grid, point) for point in low_points]
    b1, b2, b3 = sorted(basins, reverse=True)[:3]
    soln = b1 * b2 * b3
    print(f'Solution: {soln}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
