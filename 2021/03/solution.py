#!/usr/bin/env python3

def solution(lines):
    lines = list(lines)
    bits = len(lines[0])
    ones_count = [0] * bits
    items = len(lines)
    for line in lines:
        for i, val in enumerate(line):
            if val == '1':
                ones_count[i] += 1
    
    maj = [int(c > items/2) for c in ones_count]
    gamma = int(''.join(str(e) for e in maj), 2)
    epsilon = ~gamma & (2**bits - 1)
    soln = gamma * epsilon
    print(f"Solution: {soln}")
    
if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
