#!/usr/bin/env python3

from collections import defaultdict
import string

NONCHAR = '.' + string.digits

def solution(lines):
    grid = defaultdict(lambda: defaultdict(lambda: '.'))
    lines = list(lines)
    dy, dx = len(lines), len(lines[0])
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            grid[row][col] = c

    total = 0

    num = 0
    adj = False

    def terminate():
        nonlocal total, num, adj
        if adj:
            total += num
        num = 0
        adj = False


    def isadj(row, col):
        nonlocal grid
        for y in range(row-1, row+2):
            for x in range(col-1, col+2):
                if grid[y][x] not in NONCHAR:
                    return True
        return False

    for row in range(dy):
        for col in range(dx):
            c = grid[row][col]
            if c.isdigit():
                num = num * 10 + int(c)
                adj |= isadj(row, col)
            else:
                terminate()
        terminate()

    print('Solution: {}'.format(total))

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
