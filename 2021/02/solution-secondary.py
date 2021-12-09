#!/usr/bin/env python3

import operator
from functools import reduce

def parse_line(line):
    dir, amt = line.split()
    amt = int(amt)
    if dir == 'forward':
        return ('forward', amt)
    elif dir == 'down':
        return ('aim', amt)
    elif dir == 'up':
        return ('aim', -amt)
    else:
        raise Exception('bad line: {line}')
    
def solution(lines):
    ctrls = (parse_line(line) for line in lines)
    pos = [0, 0]
    aim = 0
    for inst, amt in ctrls:
        if inst == 'forward':
            pos[0] += amt
            pos[1] += aim * amt
        elif inst == 'aim':
            aim += amt
    
    soln = pos[0] * pos[1]
    print(f"Solution: {soln}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
