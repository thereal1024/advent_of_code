#!/usr/bin/env python3

import math

def solution(lines):
    times, dists = lines
    time = int(''.join(times.split()[1:]))
    dist = int(''.join(dists.split()[1:]))

    base = time / 2
    delta = (time**2 - 4*dist)**(1/2) / 2
    low = math.floor(base - delta) + 1
    high = math.ceil(base + delta) - 1
    count = high - low + 1

    print('Solution: {}'.format(count))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
