#!/usr/bin/env python3

# dy, dx
DIRS = [
    [-1, 0],
    [0, -1],
    [1, 0],
    [0, 1],
]

TARGET = 1000000000

def solution(lines):
    lines = list(lines)
    h, w = len(lines), len(lines[0])
    
    roll, square = set(), set()
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == '#':
                square.add((y, x))
            elif c == 'O':
                roll.add((y, x))
    roll = frozenset(roll)
                
    def roll_step(roll, dirn=0):
        nextroll = set()
        for y, x in roll:
            dest = y+DIRS[dirn][0], x+DIRS[dirn][1]
            if not (dest[0] in range(h) and dest[1] in range(w)):
                nextroll.add((y, x))
            elif dest in roll or dest in square:
                nextroll.add((y, x))
            else:
                nextroll.add(dest)
        return nextroll
    
    def cycle(roll):
        for d in range(4):
            while True:
                nroll = roll_step(roll, d)
                if nroll == roll:
                    break
                roll = nroll
        return frozenset(roll)
    
    def printr(r):
        for y in range(h):
            out = ''
            for x in range(w):
                p = y, x
                if p in r:
                    out += 'O'
                elif p in square:
                    out += '#'
                else:
                    out += '.'
            print(out)
                
    states = {}
    states[roll] = 0
    i = 0
    while True:
        i += 1
        roll = cycle(roll)
        if roll in states:
            base = states[roll]
            break
        else:
            states[roll] = i
    
    assert TARGET >= base
    cyclelen = i - base
    soln = ((TARGET - base) % cyclelen) + base
    sroll = next(r for r, i in states.items() if i == soln)
    
    wt = 0
    for y, _ in sroll:
        wt += h - y
    
    print(f'Solution: {wt}')


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
