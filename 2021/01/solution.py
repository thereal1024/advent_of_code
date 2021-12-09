#!/usr/bin/env python3

def solution(depths):
    deeper_measurements = 0
    last_depth = next(depths)
    for depth in depths:
        deeper_measurements += depth > last_depth
        last_depth = depth
    
    print(f"Solution: {deeper_measurements}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    depths = (int(line) for line in lines)
    solution(depths)
