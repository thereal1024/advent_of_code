#!/usr/bin/env python3

import itertools

def solution(lines):
    total = 0
    for line in lines:
        nums = list(map(int, line.split()))
        lasts = [nums[-1]]
        while not all(n == 0 for n in nums):
            nums = [b-a for a, b in itertools.pairwise(nums)]
            lasts.append(nums[-1])
        pred = sum(lasts)
        print(pred)
        total += pred

    print('Solution: {}'.format(total))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
