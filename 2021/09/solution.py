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
    
    risk = 0
    for y in range(h):
        for x in range(w):
            adj = valid_offsets(y, x, h, w)
            if all(grid[y][x] < grid[ay][ax] for ay, ax in adj):
                risk += grid[y][x] + 1
    return risk
        

def solution(lines):
    grid = parse_map(lines)
    risk = find_low_points(grid)
    print(f'Solution: {risk}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
