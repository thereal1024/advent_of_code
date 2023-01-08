#!/usr/bin/env python3

# (x,y) odd-r layout E: +x S: +y
# depends on y mod 2
OFFSETS = {
    ('e', 0): (1, 0),
    ('e', 1): (1, 0),
    ('w', 0): (-1, 0),
    ('w', 1): (-1, 0),
    ('se', 0): (0, 1),
    ('se', 1): (1, 1),
    ('sw', 0): (-1, 1),
    ('sw', 1): (0, 1),
    ('ne', 0): (0, -1),
    ('ne', 1): (1, -1),
    ('nw', 0): (-1, -1),
    ('nw', 1): (0, -1)
}

def parse_path(path):
    i = 0
    dirs = []
    while i < len(path):
        if path[i] in 'ns':
            dirs.append(path[i:i+2])
            i += 2
        else:
            dirs.append(path[i])
            i += 1
    return dirs

def single_move(pos, direc):
    pm = pos[1] % 2
    offset = OFFSETS[(direc, pm)]
    return pos[0]+offset[0], pos[1]+offset[1]

def follow_path(path):
    pos = (0, 0)
    for step in path:
        pos = single_move(pos, step)
    return pos

def solution(lines):
    paths = (parse_path(line) for line in lines)
    
    flips = set()
    for path in paths:
        dest = follow_path(path)
        if dest in flips:
            flips.remove(dest)
        else:
            flips.add(dest) 
    
    black = len(flips)
    print(f'Solution: {black}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
