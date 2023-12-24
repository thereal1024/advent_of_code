#!/usr/bin/env python3

import itertools

PLOW = 200000000000000
PHIGH = 400000000000000

def solution(lines):
    hailstones = []
    for line in lines:
        pos, vel = line.split(' @ ')
        pos = tuple(map(int, pos.split(', ')))
        vel = tuple(map(int, vel.split(', ')))
        hailstones.append((pos, vel))
    
    intersections = 0
    for (pa, va), (pb, vb) in itertools.combinations(hailstones, 2):
        det = vb[0] * va[1] - va[0] * vb[1]
        if det == 0:
            # parallel
            continue
        d0 = pb[0] - pa[0]
        d1 = pb[1] - pa[1]
        t = (vb[0] * d1 - vb[1] * d0) / det
        u = (va[0] * d1 - va[1] * d0) / det
        
        if t < 0 or u < 0:
            # intersection in the past
            continue
        ix = va[0]*t + pa[0]
        iy = va[1]*t + pa[1]
        if not ((PLOW <= ix <= PHIGH) and (PLOW <= iy <= PHIGH)):
            # not in the bounds
            continue
        intersections += 1
        
    print(f'Solution: {intersections}')


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
