#!/usr/bin/env python3

import itertools
import math

DIRS = 'LR'

def find_steps(paths, instr, start):
    instr = itertools.cycle(instr)
    loc = start
    steps = 0
    while loc[-1] != 'Z':
        direc = next(instr)
        loc = paths[loc][DIRS.index(direc)]
        steps += 1
    return steps
    
def solution(lines):
    instr, _ = next(lines),  next(lines)
    
    paths = {}
    
    for line in lines:
        name, rest = line.split(' = ')
        left, right = rest.strip('()').split(', ')
        paths[name] = (left, right)

    starts = [point for point in paths.keys() if point[-1] == 'A']
    dists = [find_steps(paths, instr, start) for start in starts]
    simsteps = math.lcm(*dists)
        
    print('Solution: {}'.format(simsteps))
        

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
