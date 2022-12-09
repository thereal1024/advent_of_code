#!/usr/bin/env python3

def parsemove(line):
    d, c = line.split(' ')
    return d, int(c)

def update_tail(head, tail):
    dx, dy = 0, 0
    # above
    if tail[1] - head[1] == 2:
        dy = 1
    # below
    elif tail[1] - head[1] == -2:
        dy = -1
    # right
    if tail[0] - head[0] == 2:
        dx = 1
    # left
    elif tail[0] - head[0] == -2:
        dx = -1
    if (dx, dy) == (0, 0):
        return tail
    return (head[0] + dx, head[1] + dy)

def solution(lines):
    moves = (parsemove(line) for line in lines)
    
    # x, y (+ is right, up)
    # head first
    knots = [(0,0)] * 10
    
    tailvisits = set([knots[-1]])

    for direc, count in moves:
        for _ in range(count):
            head = knots[0]
            if direc == 'R':
                head = (head[0] + 1, head[1])
            elif direc == 'L':
                head = (head[0] - 1, head[1])
            elif direc == 'U':
                head = (head[0], head[1] + 1)
            elif direc == 'D':
                head = (head[0], head[1] - 1)
            knots[0] = head
            # tail correction
            for i in range(len(knots)-1):
                head = knots[i]
                tail = knots[i+1]
                knots[i+1] = update_tail(head, tail)
            
            tailvisits.add(knots[-1])
    
    uniquetailvisits = len(tailvisits)
    print(f'Solution: {uniquetailvisits}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
