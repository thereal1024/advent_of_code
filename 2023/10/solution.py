#!/usr/bin/env python3

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
    
    def feed(pt, hd):
        if pt == start:
            return None
        nd = ADJ[grid[pt]] - set([DIRS[hd]])
        assert len(nd) == 1
        return next(iter(nd))
    
    head = next(iter(adj))
    path = [move(start, head)]
    head = feed(path[0], head)
    
    while path[-1] != start:
        nextp = move(path[-1], head)
        head = feed(nextp, head)
        path.append(nextp)

    farthest = len(path) // 2
    print('Solution: {}'.format(farthest))

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
