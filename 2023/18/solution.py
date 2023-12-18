#!/usr/bin/env python3

from itertools import pairwise

def area(coords):
    total = 0
    for (y1, x1), (y2, x2) in pairwise([coords[-1]] + coords):
        total += x1*y2 - x2*y1
    return total // 2

DIRS = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}
def solution(lines):
    path = set()
    point = 0, 0
    corners = []
    for line in lines:
        dirc, ct, color = line.split(' ')
        ct = int(ct)
        direc = DIRS[dirc]
        for _ in range(ct):
            point = point[0] + direc[0], point[1] + direc[1]
            path.add(point)
        corners.append(point)
        
    assert point == (0, 0)

    patharea = area(corners)
    totalarea = patharea + 1 + len(path) // 2
    print(f'Solution: {totalarea}')


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
