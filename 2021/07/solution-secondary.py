#!/usr/bin/env python3

from statistics import mean
from math import floor, ceil

def triangle(n):
    return n * (n+1) // 2

def solution(lines):
    subs = tuple(map(int, next(lines).split(',')))

    mn = mean(subs)
    mean1 = floor(mn)
    mean2 = ceil(mn)
    fuel1 = sum(triangle(abs(sub-mean1)) for sub in subs)
    fuel2 = sum(triangle(abs(sub-mean2)) for sub in subs)
    fuel = min(fuel1, fuel2)
    print(f'Solution: {fuel}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
