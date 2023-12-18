#!/usr/bin/env python3

from itertools import pairwise

def area(coords):
    total = 0
    for (y1, x1), (y2, x2) in pairwise([coords[-1]] + coords):
        total += x1*y2 - x2*y1
    return total // 2

DCODE = 'RDLU'

DIRS = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}
def solution(lines):
    pathlen = 0
    point = 0, 0
    corners = []
    for line in lines:
        dirc, ct, color = line.split(' ')
        code = color.removeprefix('(#').removesuffix(')')
        dct = int(code[:-1], 16)
        direc = DIRS[DCODE[int(code[-1])]]
        point = point[0] + direc[0] * dct, point[1] + direc[1] * dct
        pathlen += dct
        corners.append(point)
        
    assert point == (0, 0)

    patharea = area(corners)
    totalarea = patharea + 1 + pathlen // 2
    print(f'Solution: {totalarea}')


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
