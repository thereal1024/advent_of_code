#!/usr/bin/env python3

import math

def solution(lines):
    times, dists = lines
    times = map(int, times.split()[1:])
    dists = map(int, dists.split()[1:])
    poss = 1
    for time, dist in zip(times, dists):
        base = time / 2
        delta = (time**2 - 4*dist)**(1/2) / 2
        low = math.floor(base - delta) + 1
        high = math.ceil(base + delta) - 1
        count = high - low + 1
        poss *= count

    print('Solution: {}'.format(poss))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
