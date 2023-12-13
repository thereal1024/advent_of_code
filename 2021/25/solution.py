#!/usr/bin/env python3


def solution(lines):
    lines = list(lines)
    h, w = len(lines), len(lines[0])
    
    right, down = set(), set()
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == '>':
                right.add((y, x))
            elif c == 'v':
                down.add((y, x))

    def shift(rt, dn):
        newrt = set()
        for y, x in rt:
            dest = y, (x+1) % w
            if dest not in rt and dest not in dn:
                newrt.add(dest)
            else:
                newrt.add((y, x))
        newdn = set()
        for y, x in dn:
            dest = (y+1) % h, x
            if dest not in newrt and dest not in dn:
                newdn.add(dest)
            else:
                newdn.add((y, x))
        return newrt, newdn
    
    n = 0
    while True:
        newrt, newdn = shift(right, down)
        n += 1
        if newrt == right and newdn == down:
            break
        right, down = newrt, newdn
    
    print(f'Solution: {n}')
    
    
if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
