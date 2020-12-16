#!/usr/bin/env python3

from collections import Counter

WINDOW = 25

def find_wrong_number(nums, window):
    for i in range(window, len(nums)):
        lookback_start = i - window
        target = nums[i]
        lookback_set = Counter(nums[lookback_start:i])
        valid = False
        for first_possible_num in lookback_set:
            needed = target - first_possible_num
            if needed in lookback_set:
                if needed == first_possible_num and lookback_set[needed] < 2:
                    continue
                valid = True
                break
        if not valid:
            return target
    return None

def solution(lines):
    nums = [int(line) for line in lines]
    wrong_number = find_wrong_number(nums, WINDOW)
    print(f"Solution: {wrong_number}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
