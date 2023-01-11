#!/usr/bin/env python3

def parse_line(line):
    s, e = line.split(' -> ')
    s = tuple(map(int, s.split(',')))
    e = tuple(map(int, e.split(',')))
    return s, e

def mark_lines(lines):
    grid = {}
    for line in lines:
        (sx, sy), (ex, ey) = line
        if sx == ex:
            sy, ey = sorted((sy, ey))
            for y in range(sy, ey+1):
                p = (sx, y)
                if p in grid:
                    grid[p] += 1
                else:
                    grid[p] = 1
            pass # vert dy
        elif sy == ey:
            sx, ex = sorted((sx, ex))
            for x in range(sx, ex+1):
                p = (x, sy)
                if p in grid:
                    grid[p] += 1
                else:
                    grid[p] = 1
        # skip if not H/V
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
