#!/usr/bin/env python3

DAYS = 80

NEW_START = 8
CYCLE = 7

def step_day(fish):
    next_fish = []
    new = 0
    for f in fish:
        if f == 0:
            new += 1
            f = CYCLE
        f -= 1
        next_fish.append(f)
    next_fish += [NEW_START] * new
    return tuple(next_fish)

def solution(lines):
    fish = tuple(map(int, next(lines).split(',')))
    for _ in range(DAYS):
        fish = step_day(fish)
    count = len(fish)
    print(f'Solution: {count}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
