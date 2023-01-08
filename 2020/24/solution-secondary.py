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

ROUNDS = 100

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

def get_adj(pos):
    pm = pos[1] % 2
    return set((pos[0]+dx, pos[1]+dy) for (_, m), (dx, dy) in OFFSETS.items() if m == pm)

def life_round(blackset):
    minx = min(x for x, _ in blackset) - 1
    maxx = max(x for x, _ in blackset) + 1
    miny = min(y for _, y in blackset) - 1
    maxy = max(y for _, y in blackset) + 1
    
    newbl = set()

    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            pos = (x, y)
            adj = get_adj(pos)
            blc = len(blackset & adj)
            if pos in blackset:
                if blc == 1 or blc == 2:
                    newbl.add(pos)
            elif blc == 2: # white tile, adj 2 black, flip
                newbl.add(pos)
    
    return newbl

def solution(lines):
    paths = (parse_path(line) for line in lines)
    
    blackset = set()
    for path in paths:
        dest = follow_path(path)
        if dest in blackset:
            blackset.remove(dest)
        else:
            blackset.add(dest) 
    
    for i in range(ROUNDS):
        blackset = life_round(blackset)
    
    black = len(blackset)
    print(f'Solution: {black}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
