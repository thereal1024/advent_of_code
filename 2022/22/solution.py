#!/usr/bin/env python3

import re

# (y, x)
DIRS = [
    (0, 1), # r
    (1, 0), # d
    (0, -1), # l
    (-1, 0) # u
]

TURNS = {
    'L': -1,
    'R': 1,
    None: 0
}

def parse_grid(section):
    grid = sections[0].split('\n')
    width = max(len(row) for row in grid)
    grid = [row + ' '*(width-len(row)) for row in grid] 
    return grid

def parse_cmds(line):
    cmds = []
    for match in re.finditer(r'(\d+)(L|R)?', line):
        dist = int(match.group(1))
        turn = TURNS[match.group(2)] # might be None
        cmds.append((dist, turn))
    return cmds

def walk(grid, cmds):
    h, w = len(grid), len(grid[0])
    # y, x
    pos = (0, grid[0].index('.'))
    direc = 0
    
    for dist, turn in cmds:
        dirvec = DIRS[direc]
        for _ in range(dist):
            npos = ((pos[0]+dirvec[0]) % h, (pos[1]+dirvec[1]) % w)
            while grid[npos[0]][npos[1]] == ' ':
                npos = ((npos[0]+dirvec[0]) % h, (npos[1]+dirvec[1]) % w)
            if grid[npos[0]][npos[1]] == '#':
                break
            pos = npos
        direc = (direc + turn) % len(DIRS)

    return pos, direc


def solution(sections):
    grid = parse_grid(sections[0])
    cmds = parse_cmds(sections[1])
    
    (y, x), direc = walk(grid, cmds) 
    soln = 1000 * (y+1) + 4 * (x+1) + direc
    print(f'Solution: {soln}')


if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
