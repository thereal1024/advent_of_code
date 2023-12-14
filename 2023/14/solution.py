#!/usr/bin/env python3

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
                
    def roll_step(roll):
        nextroll = set()
        for y, x in roll:
            if y == 0:
                nextroll.add((y, x))
                continue
            dest = y-1, x
            if dest in roll or dest in square:
                nextroll.add((y, x))
            else:
                nextroll.add(dest)
        return nextroll
    
    while True:
        nroll = roll_step(roll)
        if nroll == roll:
            break
        roll = nroll
    
    wt = 0
    for y, _ in roll:
        wt += h - y
    
    print(f'Solution: {wt}')


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
