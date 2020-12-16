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

def find_contiguous_sum_property(nums, target):
    lb = 0
    rb = 0
    running_total = 0
    while running_total != target and rb <= len(nums):
        if running_total < target:
            running_total += nums[rb]
            rb += 1
        elif running_total > target:
            running_total -= nums[lb]
            lb += 1
    if running_total != target:
        raise Exception('bounds not found')
    seq = nums[lb:rb]
    return min(seq) + max(seq)
            

def solution(lines):
    nums = [int(line) for line in lines]
    wrong_number = find_wrong_number(nums, WINDOW)
    soln = find_contiguous_sum_property(nums, wrong_number)
    print(f"Solution: {soln}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
