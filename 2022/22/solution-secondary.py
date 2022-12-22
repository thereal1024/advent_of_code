#!/usr/bin/env python3

#
# IMPORTANT: This solution hardcodes the particular cube folding of my input.
#

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

# manual input analysis
SIDE = 50
# side1, side2, leave1, leave2, reverse
ADJ = [
    (0, 3, 2, 2, True),
    (0, 5, 3, 2, False),
    (1, 2, 1, 0, False),
    (1, 4, 0, 0, True),
    (1, 5, 3, 1, False),
    (2, 3, 2, 3, False),
    (4, 5, 1, 0, False)
]
# end manual input analysis

# # manual test input analysis
# SIDE = 4
# # side1, side2, leave1, leave2, reverse
# ADJ = [
#     (0, 1, 3, 3, True),
#     (0, 2, 2, 3, False),
#     (0, 5, 0, 0, True),
#     (1, 4, 1, 1, True),
#     (1, 5, 2, 1, True),
#     (2, 4, 1, 2, True),
#     (3, 5, 0, 3, True)
# ]
# # end manual test input analysis

DIRBASE = [
    (0, SIDE - 1),
    (SIDE - 1, 0),
    (0, 0),
    (0, 0)
]

def adj_map():
    amap = {}
    for s1, s2, l1, l2, rev in ADJ:
        amap[(s1, l1)] = (s2, l2, rev)
        amap[(s2, l2)] = (s1, l1, rev)
    return amap
        
ADJMAP = adj_map()

def parse_grid(section):
    grid = sections[0].split('\n')
    width = max(len(row) for row in grid)
    grid = [row + ' '*(width-len(row)) for row in grid]
    
    h, w = len(grid), len(grid[0])
    hl, wl = h//SIDE, w//SIDE
    
    
    i = 0
    sidepos = {}
    for y in range(hl):
        for x in range(wl):
            if grid[y*SIDE][x*SIDE] in '.#':
                sidepos[(y, x)] = i
                sidepos[i] = (y, x)
                i += 1

    assert i == 6
    
    return grid, sidepos

def parse_cmds(line):
    cmds = []
    for match in re.finditer(r'(\d+)(L|R)?', line):
        dist = int(match.group(1))
        turn = TURNS[match.group(2)] # might be None
        cmds.append((dist, turn))
    return cmds

def cross_side(grid, sidepos, pos, direc):
    yl, xl = pos[0]//SIDE, pos[1]//SIDE
    ys, xs = pos[0] % SIDE, pos[1] % SIDE
    
    start_side = sidepos[(yl,xl)]
    offset = [ys, xs, ys, xs][direc]
    
    new_side, en_direc, rev = ADJMAP[(start_side, direc)]
    new_base = (sidepos[new_side][0] * SIDE, sidepos[new_side][1] * SIDE)
    new_offset = (SIDE - 1 - offset) if rev else offset
    side_base = (new_base[0] + DIRBASE[en_direc][0], new_base[1] + DIRBASE[en_direc][1])
    if en_direc in (0, 2):
        new_pos = (side_base[0] + new_offset, side_base[1])
    elif en_direc in (1, 3):
        new_pos = (side_base[0], side_base[1] + new_offset)
    new_direc = (en_direc + 2) % len(DIRS)
    return new_pos, new_direc

def walk(grid, sidepos, cmds):
    h, w = len(grid), len(grid[0])
    # y, x
    pos = (0, grid[0].index('.'))
    direc = 0
    
    for dist, turn in cmds:
        for _ in range(dist):
            dirvec = DIRS[direc]
            ndirec = direc
            npos = (pos[0]+dirvec[0], pos[1]+dirvec[1])
            if not (0 <= npos[0] < h and 0 <= npos[1] < w) or grid[npos[0]][npos[1]] == ' ':
                npos, ndirec = cross_side(grid, sidepos, pos, direc)
            if grid[npos[0]][npos[1]] == '#':
                break
            pos = npos
            direc = ndirec
        direc = (direc + turn) % len(DIRS)

    return pos, direc


def solution(sections):
    grid, sidepos = parse_grid(sections[0])
    cmds = parse_cmds(sections[1])
    (y, x), direc = walk(grid, sidepos, cmds) 
    soln = 1000 * (y+1) + 4 * (x+1) + direc
    print(f'Solution: {soln}')


if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
