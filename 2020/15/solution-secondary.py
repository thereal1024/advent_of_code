#!/usr/bin/env python3

END = 30 * 1000 * 1000

# This takes 1 GiB of memory. Maybe it can be optimized?

def solution(lines):
    nums = [int(e) for e in next(lines).split(',')]
    last_seen = dict((n, i) for i, n in enumerate(nums[:-1]))
    
    for i in range(len(nums), END):
        last = nums[i - 1]
        is_first_seen = last not in last_seen
        last_rel = i - 1 - last_seen[last] if not is_first_seen else None
        last_seen[last] = i - 1
        if is_first_seen:
            nums.append(0)
        else:
            nums.append(last_rel)
    
    soln = nums[-1]
    print(f"Solution: {soln}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
