#!/usr/bin/env python3

import itertools

def solution(lines):
    total = 0
    for line in lines:
        nums = list(map(int, line.split()))
        firsts = [nums[0]]
        while not all(n == 0 for n in nums):
            nums = [b-a for a, b in itertools.pairwise(nums)]
            firsts.append(nums[0])
        pred = 0
        for f in reversed(firsts[:-1]):
            pred = f - pred
        print(pred)
        total += pred

    print('Solution: {}'.format(total))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
