#!/usr/bin/env python3

from functools import cache

SCALE = 5

@cache
def countall(row, spgs):
    if row == '':
        return int(len(spgs) == 0)
    
    f = row[0]
    if f == ' ':
        return countall(row[1:], spgs)
    elif f == '#':
        return expect(row, spgs)
    elif f == '?':
        return countall(row[1:], spgs) + expect(row, spgs)
    else:
        raise Exception()

@cache
def expect(row, spgs):
    if len(spgs) == 0:
        return 0
    
    nexl = spgs[0]
    if len(row) < nexl:
        return 0
    
    if not all(c == '#' or c == '?' for c in row[:nexl]):
        return 0
    
    if len(row) == nexl:
        return int(len(spgs) == 1)
    
    if row[nexl] == '#':
        return 0
    
    return countall(row[nexl+1:], spgs[1:])

def solution(lines):
    total = 0
    for line in lines:
        row, spgs = line.split(' ')
        row = row.replace('.', ' ')
        spgs = tuple(map(int, spgs.split(',')))

        row = '?'.join(row for _ in range(SCALE))
        spgs = spgs * SCALE
 
        total += countall(row, spgs)

    
    print('Solution: {}'.format(total))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
