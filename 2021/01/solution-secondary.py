#!/usr/bin/env python3

from collections import deque

def solution(depths):
    deeper_measurements = 0
    depth_queue = deque([next(depths), next(depths), next(depths)])
    last_depth_sum = sum(depth_queue)
    for depth in depths:
        depth_sum = last_depth_sum + depth - depth_queue.popleft() 
        depth_queue.append(depth)
        deeper_measurements += depth_sum > last_depth_sum
        last_depth_sum = depth_sum
    
    print(f"Solution: {deeper_measurements}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    depths = (int(line) for line in lines)
    solution(depths)
