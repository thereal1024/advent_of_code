#!/usr/bin/env python3

import itertools

ROUNDS = 100

OFFSETS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
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

def take_step(grid):
    h = len(grid)
    w = len(grid[0])
    
    
    for y in range(h):
        for x in range(w):
            grid[y][x] += 1
    
    flashed = set()
    while any(o > 9 for row in grid for o in row):
        for y in range(h):
            for x in range(w):
                if grid[y][x] > 9:
                    grid[y][x] = 0
                    flashed.add((y, x))
                    adj = set(valid_offsets(y, x, h, w)) - flashed
                    for ay, ax in adj:
                        grid[ay][ax] += 1
    
    return len(flashed)


def solution(lines):
    grid = parse_map(lines)
    grid_size = len(grid) * len(grid[0])
    for i in itertools.count(1):
        if take_step(grid) == grid_size:
            break
    print(f'Solution: {i}')
    

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
