#!/usr/bin/env python3

import itertools

DIRS = 'LR'

def solution(lines):
    instr, _ = next(lines),  next(lines)
    instr = itertools.cycle(instr)
    
    paths = {}
    
    for line in lines:
        name, rest = line.split(' = ')
        left, right = rest.strip('()').split(', ')
        paths[name] = (left, right)

    loc = 'AAA'
    steps = 0
    while loc != 'ZZZ':
        direc = next(instr)
        loc = paths[loc][DIRS.index(direc)]
        steps += 1
        
    print('Solution: {}'.format(steps))
        

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
