#!/usr/bin/env python3

import itertools
from functools import cache

# dy, dx
# RLDU
DIRS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

STEPS = 26501365

def solution(lines):
    lines = list(lines)
    h, w = len(lines), len(lines[0])
    
    assert h == w
    
    spaces = set()
    start = None
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c != '#':
                spaces.add((y, x))
            if c == 'S':
                assert start == None
                start = y, x
    
    def step(points):
        newpoints = set()
        for point in points:
            for dir in DIRS:
                newpoint = point[0] + dir[0], point[1] + dir[1]
                if newpoint in spaces:
                    newpoints.add(newpoint)
        return frozenset(newpoints)
    
    @cache
    def maltpoints(malt, dir):
        if dir[0] == -1: # dy in coord
            return frozenset((-1, x) for x in range(w) if (h-1, x) in malt)
        elif dir[0] == 1:
            return frozenset((h, x) for x in range(w) if (0, x) in malt)
        elif dir[1] == -1: # dx in coord
            return frozenset((y, -1) for y in range(h) if (y, w-1) in malt)
        elif dir[1] == 1:
            return frozenset((y, w) for y in range(h) if (y, 0) in malt)
        else:
            raise Exception()

    @cache
    def crossstep(points, sidepoints):
        newpoints = set()
        for point in itertools.chain(points, itertools.chain(*sidepoints)):
            for dir in DIRS:
                newpoint = point[0] + dir[0], point[1] + dir[1]
                if newpoint in spaces:
                    newpoints.add(newpoint)
        return frozenset(newpoints)
    
    def bigstep(metapoints):
        newmetapoints = {}
        newdupcoords = set()
        
        def boundarystep(dupcoord, points, extend):
            sidepoints = []
            for dir in DIRS:
                altdupcoord = dupcoord[0] + dir[0], dupcoord[1] + dir[1]
                if altdupcoord in metapoints:
                    malt = metapoints[altdupcoord]
                    sidepoints.append(maltpoints(malt, dir))
                elif extend:
                    newdupcoords.add(altdupcoord)
            sidepoints = tuple(sidepoints)
            crosspoints = crossstep(points, sidepoints)
            if len(crosspoints) > 0:
                newmetapoints[dupcoord] = crosspoints
        
        for dupcoord, points in metapoints.items():
            boundarystep(dupcoord, points, True)
        for dupcoord in newdupcoords:
            boundarystep(dupcoord, frozenset(), False)
        return newmetapoints
    
    scale, rem = divmod(STEPS, h)
    extvals = []

    metapoints = {(0, 0): frozenset({start})}
    for i in range(1, 5001):
        metapoints = bigstep(metapoints)

        if i % h == rem:
            npoints = sum(len(p) for p in metapoints.values())
            extvals.append(npoints)
            if len(extvals) == 3:
                break

    constant = extvals[0]
    linear = extvals[1] - extvals[0]
    linear2 = extvals[2] - extvals[1]
    quad = linear2 - linear
    plots  = constant + linear * scale + (scale * (scale - 1) // 2) * quad
    print(f'Solution: {plots}')
    

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
