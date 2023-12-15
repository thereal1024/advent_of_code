#!/usr/bin/env python3

def compress(val, c):
    val += ord(c)
    val *= 17
    val %= 256
    return val
    
def hash(s):
    val = 0
    for c in s:
        val = compress(val, c)
    return val

def solution(lines):
    lines = list(lines)
    assert len(lines) == 1
    steps = lines[0].split(',')
    total = 0
    for step in steps:
        total += hash(step)
    print(f'Solution: {total}')


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
