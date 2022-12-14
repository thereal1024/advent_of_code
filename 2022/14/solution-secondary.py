#!/usr/bin/env python3

import itertools

SOURCE = (500, 0)

REL = [0, -1, 1]

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def dimensions(paths):
    xmax = SOURCE[0]
    ymax = SOURCE[1]
    xmin = SOURCE[0]
    ymin = SOURCE[1]
    for path in paths:
        for x, y in path:
            xmax = max(xmax, x)
            ymax = max(ymax, y)
            xmin = min(xmin, x)
            ymin = min(ymin, y)
            
    xmin = min(xmin, SOURCE[0]-(ymax+2))
    xmax = max(xmax, SOURCE[0]+(ymax+2))
            
    return xmin - 1, ymin, xmax + 1, ymax + 2

def create_grid(paths):
    xmin, ymin, xmax, ymax = dimensions(paths)
    assert ymin == 0
    w = xmax - xmin + 1
    h = ymax - ymin + 1
    
    grid = [bytearray(b'.'*w) for _ in range(h-1)]
    grid.append(bytearray(b'#'*w))
    paths = [[(x-xmin,y-ymin) for x, y in path] for path in paths]
    
    for path in paths:
        for (xs, ys), (xe, ye) in pairwise(path):
            if xs == xe:
                ys, ye = sorted((ys, ye))
                for y in range(ys, ye+1):
                    grid[y][xs] = ord('#')
            elif ys == ye:
                xs, xe = sorted((xs, xe))
                for x in range(xs, xe+1):
                    grid[ys][x] = ord('#')
    
    
    #print(xmin, ymin, xmax, ymax)
    src = (SOURCE[0]-xmin, SOURCE[1]-ymin)
    return grid, src

def render_grid(grid):
    return '\n'.join(line.decode() for line in grid)

def parse_path(line):
    points = line.split(' -> ')
    return [tuple(map(int,point.split(','))) for point in points]

def simulate_sand(grid, src):
    h = len(grid)
    settled = 0
    done = False
    while True:
        pos = src
        while True:
            yp = pos[1] + 1
            moved = False
            for xp in [pos[0]+dx for dx in REL]:
                if grid[yp][xp] == ord('.'):
                    pos = (xp, yp)
                    moved = True
                    break
            if not moved:
                break
        grid[pos[1]][pos[0]] = ord('o')
        settled += 1
        if pos == src:
            break
    return settled
            

def solution(lines):
    paths = [parse_path(line) for line in lines]
    grid, src = create_grid(paths)
    settled = simulate_sand(grid, src)
    print(f'Solution: {settled}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
