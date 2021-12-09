#!/usr/bin/env python3

import operator
from functools import reduce

def parse_line(line):
    dir, amt = line.split()
    amt = int(amt)
    if dir == 'forward':
        return (amt, 0)
    elif dir == 'down':
        return (0, amt)
    elif dir == 'up':
        return (0, -amt)
    else:
        raise Exception('bad line: {line}')
    
def solution(lines):
    ctrls = (parse_line(line) for line in lines)
    coords = reduce(lambda a, b: tuple(map(operator.add, a, b)), ctrls)
    soln = coords[0] * coords[1]
    print(f"Solution: {soln}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
