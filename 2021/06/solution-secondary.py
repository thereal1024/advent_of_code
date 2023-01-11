#!/usr/bin/env python3

from collections import defaultdict

DAYS = 256

NEW_START = 8
CYCLE = 7

def step_day(fish):
    next_fish = defaultdict(int)
    for f, count in fish.items():
        if f == 0:
            next_fish[NEW_START] += count
            f = CYCLE
        f -= 1
        next_fish[f] += count
    return next_fish

def solution(lines):
    fish = tuple(map(int, next(lines).split(',')))
    fish = dict((n, fish.count(n)) for n in range(NEW_START+1))
    for _ in range(DAYS):
        fish = step_day(fish)
    count = sum(fish.values())
    print(f'Solution: {count}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
