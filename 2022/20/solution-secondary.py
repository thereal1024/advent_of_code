#!/usr/bin/env python3

COORDS = [1000, 2000, 3000]
KEY = 811589153
ROUNDS = 10

def solution(lines):
    nums = list(enumerate(int(line) * KEY for line in lines))

    numlen = len(nums)
    for _ in range(ROUNDS):
        for inidx in range(numlen):
            num_idx, num = next((i, num) for i, (ii, num) in enumerate(nums) if ii == inidx)
            inspos = (num_idx + num) % (numlen - 1)
            nums.pop(num_idx)
            nums.insert(inspos, (inidx, num))

    zero_idx = next(i for i, (_, num) in enumerate(nums) if num == 0)
    coordvals = [nums[(zero_idx + coord) % numlen][1] for coord in COORDS]
    soln = sum(coordvals)
    print(f'Solution: {soln}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
