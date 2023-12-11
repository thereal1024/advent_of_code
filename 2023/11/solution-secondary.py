#!/usr/bin/env python3

import itertools

EMPTYSCALE = 1000000

def solution(lines):
    
    lines = list(lines)
    h, w = len(lines), len(lines[0])
    
    emptyrow = [True] * h
    emptycol = [True] * w
    
    points = set()
    
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == '#':
                points.add((y, x))
                emptyrow[y] = False
                emptycol[x] = False
            else:
                assert c == '.'
                
    def prefixsum(arr):
        total = [int(arr[0])]
        for i in range(1, len(arr)):
            total.append(total[i-1] + arr[i])
        return total
            
    emptyrow = prefixsum(emptyrow)
    emptycol = prefixsum(emptycol)
    
    def dist(s, e):
        scalar = abs(e[0] - s[0]) + abs(e[1] - s[1])
        yl, yh = sorted([s[0], e[0]])
        exy = emptyrow[yh] - emptyrow[yl]
        xl, xh = sorted([s[1], e[1]])
        exx = emptycol[xh] - emptycol[xl]
        return scalar + (exy + exx) * (EMPTYSCALE - 1)
    
    totaldist = sum(dist(p1, p2) for p1, p2 in itertools.combinations(points, 2))
    print('Solution: {}'.format(totaldist))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
