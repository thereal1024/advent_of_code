#!/usr/bin/env python3

def solution(lines):
    ordered_adapters = [0] + sorted(int(num) for num in lines)
    ordered_adapters += [ordered_adapters[-1] + 3]
    diff_list = [ordered_adapters[i+1] - ordered_adapters[i] for i in range(len(ordered_adapters) - 1)]
    ones = diff_list.count(1)
    threes = diff_list.count(3)
    soln = ones * threes
    print(f"Solution: {soln}")
    
if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
