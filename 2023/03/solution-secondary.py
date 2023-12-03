#!/usr/bin/env python3

from collections import defaultdict

def solution(lines):
    grid = defaultdict(lambda: defaultdict(lambda: '.'))
    lines = list(lines)
    dy, dx = len(lines), len(lines[0])
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            grid[row][col] = c

    gears = defaultdict(list)

    num = 0
    adj = None

    def terminate():
        nonlocal gears, num, adj
        if adj:
            gears[adj].append(num)
        num = 0
        adj = None


    def isadj(row, col):
        nonlocal adj, grid
        for y in range(row-1, row+2):
            for x in range(col-1, col+2):
                if grid[y][x] == '*':
                    loc = y, x
                    assert adj is None or adj == loc
                    adj = loc

    for row in range(dy):
        for col in range(dx):
            c = grid[row][col]
            if c.isdigit():
                num = num * 10 + int(c)
                isadj(row, col)
            else:
                terminate()
        terminate()

    total = 0
    for gearnums in gears.values():
        if len(gearnums) == 2:
            total += gearnums[0] * gearnums[1]

    print('Solution: {}'.format(total))
    

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
