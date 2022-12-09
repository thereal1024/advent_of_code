#!/usr/bin/env python3

def parsemove(line):
    d, c = line.split(' ')
    return d, int(c)

def solution(lines):
    moves = (parsemove(line) for line in lines)
    
    # x, y (+ is right, up)
    head = (0, 0)
    tail = (0, 0)
    
    tailvisits = set([tail])

    for direc, count in moves:
        for _ in range(count):
            if direc == 'R':
                head = (head[0] + 1, head[1])
            elif direc == 'L':
                head = (head[0] - 1, head[1])
            elif direc == 'U':
                head = (head[0], head[1] + 1)
            elif direc == 'D':
                head = (head[0], head[1] - 1)
            # tail correction
            # above
            if tail[1] - head[1] == 2:
                tail = (head[0], head[1] + 1)
            # below
            elif tail[1] - head[1] == -2:
                tail = (head[0], head[1] - 1)
            # right
            elif tail[0] - head[0] == 2:
                tail = (head[0] + 1, head[1])
            # left
            elif tail[0] - head[0] == -2:
                tail = (head[0] - 1, head[1])
            
            tailvisits.add(tail)
    
    uniquetailvisits = len(tailvisits)
    print(f'Solution: {uniquetailvisits}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
