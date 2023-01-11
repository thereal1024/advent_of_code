#!/usr/bin/env python3

def parse_line(line):
    s, e = line.split(' -> ')
    s = tuple(map(int, s.split(',')))
    e = tuple(map(int, e.split(',')))
    return s, e

def mark_lines(lines):
    grid = {}
    
    def add_p(p):
        nonlocal grid
        if p in grid:
            grid[p] += 1
        else:
            grid[p] = 1
    
    for line in lines:
        (sx, sy), (ex, ey) = line
        if sx == ex:
            sy, ey = sorted((sy, ey))
            for y in range(sy, ey+1):
                add_p((sx, y))
                
            pass # vert dy
        elif sy == ey:
            sx, ex = sorted((sx, ex))
            for x in range(sx, ex+1):
                add_p((x, sy))
        else:
            assert abs(ey-sy) == abs(ex-sx)
            if ex > sx:
                rx = range(sx, ex+1)
            else:
                rx = range(sx, ex-1, -1)
            if ey > sy:
                ry = range(sy, ey+1)
            else:
                ry = range(sy, ey-1, -1)
            for x, y in zip(rx, ry):
                add_p((x, y))
    
    return grid

def solution(lines):
    lines = (parse_line(line) for line in lines)
    grid = mark_lines(lines)
    overlap_points = sum(1 for l in grid.values() if l > 1)
    print(f'Solution: {overlap_points}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
