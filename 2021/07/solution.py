#!/usr/bin/env python3

from statistics import median

def solution(lines):
    subs = tuple(map(int, next(lines).split(',')))

    med = round(median(subs))
    fuel = sum(abs(sub-med) for sub in subs)
    print(f'Solution: {fuel}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
