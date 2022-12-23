#!/usr/bin/env python3


from collections import defaultdict
import itertools
from tqdm import tqdm

# y  x
# +y down, +x right
DEF_REL = [
    [(-1, 0), (-1, -1), (-1, 1)], # N/u
    [(1, 0), (1, -1), (1, 1)], # S/d
    [(0, -1), (-1, -1), (1, -1)], # W/l
    [(0, 1), (-1, 1), (1, 1)] # E/r
]

ADJ = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

def positions(lines):
    grid = list(lines)
    out = set()
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if grid[y][x] == '#':
                out.add((y,x))
    return frozenset(out)

def def_rel_n(n):
    n = n % len(DEF_REL)
    return DEF_REL[n:] + DEF_REL[:n]

def do_round(allpos, n):
    rot_def_rel = def_rel_n(n)
    proposals = defaultdict(list)
    for py, px in allpos:
        if all(((py+dy, px+dx) not in allpos) for dy, dx in ADJ):
            continue
        for rel in rot_def_rel:
            if all(((py+dy, px+dx) not in allpos) for dy, dx in rel):
                dy, dx = rel[0]
                proposals[(py+dy, px+dx)].append((py, px))
                break
    newpos = set(allpos)
    for dest, starts in proposals.items():
        if len(starts) == 1:
            newpos.remove(starts[0])
            newpos.add(dest)
    
    return frozenset(newpos)
    

def printpos(allpos):
    miny = min(y for y, _ in allpos)
    maxy = max(y for y, _ in allpos)
    minx = min(x for _, x in allpos)
    maxx = max(x for _, x in allpos)
    
    vis = '\n'.join(''.join('.#'[(y, x) in allpos] for x in range(minx, maxx+1)) for y in range(miny, maxy+1))
    print(vis)
    print()

def simulate(allpos):   
    for n in tqdm(itertools.count(), unit='rounds'):
        nextpos = do_round(allpos, n)
        if nextpos == allpos:
            return n+1
        allpos = nextpos

def count_empty(allpos):
    miny = min(y for y, _ in allpos)
    maxy = max(y for y, _ in allpos)
    minx = min(x for _, x in allpos)
    maxx = max(x for _, x in allpos)
    
    empty = 0
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if (y, x) not in allpos:
                empty += 1
    return empty

def solution(lines):
    allpos = positions(lines)
    nomoveround = simulate(allpos)
    print(f'Solution: {nomoveround}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
