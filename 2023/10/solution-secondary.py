#!/usr/bin/env python3

import itertools

# dy, dx row, col
N = (-1, 0)
S = (1, 0)
E = (0, 1)
W = (0, -1)

DIRS = {
    N: S,
    S: N,
    E: W,
    W: E,
}

RT90 = {
    N: E,
    S: W,
    E: S,
    W: N,
}

LT90 = {
    N: W,
    S: E,
    E: N,
    W: S,
}

ADJ = {
    '|': set([N, S]),
    '-': set([E, W]),
    'L': set([N, E]),
    'J': set([N, W]),
    '7': set([S, W]),
    'F': set([S, E]),
}

def move(point, dir):
    return point[0] + dir[0], point[1] + dir[1]

def solution(lines):
    
    grid = {}
    start = None
    
    lines = list(lines)
    h, w = len(lines), len(lines[0])
    
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(y, x)] = c
            if c == 'S':
                assert start == None
                start = (y, x)
    
    adj = set()
    for dir in DIRS.keys():
        cand = move(start, dir)
        # revserse of move avail in candidate direction
        if cand in grid and grid[cand] in ADJ and DIRS[dir] in ADJ[grid[cand]]:
            adj.add(dir)
    assert len(adj) == 2
    
    
    ihead = next(iter(adj))
    
    def feed(pt, hd):
        if pt == start:
            return ihead
        nd = ADJ[grid[pt]] - set([DIRS[hd]])
        assert len(nd) == 1
        return next(iter(nd))
    
    path = [move(start, ihead)]
    head = [feed(path[0], ihead)]
    
    while path[-1] != start:
        nextp = move(path[-1], head[-1])
        head.append(feed(nextp, head[-1]))
        path.append(nextp)
    
    def bounded(point):
        return point[0] in range(h) and point[1] in range(w)
    
    # follow the path and sweep both left and right until hit another path point
    # left and right needs to be applied to both the incoming and outgoing direction
    # either the left or right accummulated point set could be the one needed
    # if we hit the map edge on a sweep, that direction is wrong
    pathset = set(path)
    lpts, rpts = set(), set()
    lburned, rburned = False, False
    angles = itertools.pairwise([head[-1]] + head[:-1])
    for point, heads in zip(path, angles):
        for head in heads:
            ldir = LT90[head]
            lp = move(point, ldir)
            while bounded(lp) and lp not in pathset:
                lpts.add(lp)
                lp = move(lp, ldir)
            if not bounded(lp):
                lburned = True

            rdir = RT90[head]
            rp = move(point, rdir)
            while bounded(rp) and rp not in pathset:
                rpts.add(rp)
                rp = move(rp, rdir)
            if not bounded(rp):
                rburned = True

    assert lburned != rburned
    if not lburned:
        area = len(lpts)
    elif not rburned:
        area = len(rpts)
        
    print('Solution: {}'.format(area))
        

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
