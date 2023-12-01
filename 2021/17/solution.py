#!/usr/bin/env python3

def parse_target(line):
    line = line.removeprefix('target area: ')
    x, y = line.split(', ')
    lx, hx = map(int, x.removeprefix('x=').split('..'))
    ly, hy = map(int, y.removeprefix('y=').split('..'))
    return (lx, hx), (ly, hy)


def simulate(sv, target):
    px, py = (0, 0)
    vx, vy = sv
    (lx, hx), (ly, hy) = target
    highest_y = py
    while px <= hx and py >= ly:
        px += vx
        py += vy
        vx = max(0, vx - 1)
        vy = vy - 1
        highest_y = max(highest_y, py)
        if lx <= px <= hx and ly <= py <= hy:
            return True, highest_y
    return False, highest_y

def find_highest_y(target):
    (_, hx), (ly, _) = target
    highest = float('-inf')
    for vx in range(1, hx+1):
        for vy in range(-abs(ly), abs(ly)):
            hit, test_highest = simulate((vx, vy), target)
            if hit:
                highest = max(highest, test_highest)
    return highest

def solution(lines):
    target = parse_target(next(lines))
    highest = find_highest_y(target)
    print(f'Solution: {highest}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
