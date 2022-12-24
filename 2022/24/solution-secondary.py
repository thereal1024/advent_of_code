#!/usr/bin/env python3

from collections import defaultdict
import functools
import itertools

MOVE = {
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
    '^': (-1, 0)
}

PMOVE = [
    (0, 0),
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def parse_map(lines):

    grid = list(lines)
    h, w = len(grid), len(grid[0])
    blz = defaultdict(str)
    for y, row in enumerate(grid):
        if y == 0:
            startx = row.index('.') - 1
            assert startx == 0
            continue
        elif y == h-1:
            endx = row.index('.') - 1
            assert endx == w-3
            continue
        for x, c in enumerate(row):
            if x == 0 or x == w-1:
                assert c == '#'
            if c in '^v<>':
                blz[(y-1, x-1)] += c
    h = h - 2
    w = w - 2

    @functools.cache
    def get_map_step(n):
        if n == 0:
            nonlocal blz
            return blz
        nonlocal h, w
        pblz = get_map_step(n-1)
        nblz = defaultdict(str)
        for pos, bls in pblz.items():
            for bl in bls:
                npos = ((pos[0]+MOVE[bl][0]) % h, (pos[1]+MOVE[bl][1]) % w)
                nblz[npos] += bl
        return nblz

    return get_map_step, (h, w)

def mapwalk(mprov, hw, rev, starttime):
    h, w = hw
    start = (-1, 0)
    end = (h, w-1)
    if rev:
        start, end = end, start

    atpos = set([start])
    for n in itertools.count(1):
        mp = mprov(starttime + n)
        nextatpos = set()
        for y, x in atpos:
            for dy, dx in PMOVE:
                npos = (y+dy, x+dx)
                if not ((npos[0] in range(h) and npos[1] in range(w)) or npos in (start, end)):
                    continue
                if npos in mp:
                    continue
                nextatpos.add(npos)
        atpos = nextatpos
        if end in atpos:
            break
    
    return n

def solution(lines):
    mapprov, hw = parse_map(lines)
    there_t = mapwalk(mapprov, hw, False, 0)
    back_t = mapwalk(mapprov, hw, True, there_t)
    again_t =  mapwalk(mapprov, hw, False, there_t+back_t)
    soln = there_t + back_t + again_t
    print(f'Solution: {soln}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
