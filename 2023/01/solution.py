#!/usr/bin/env python3

def solution(lines):
    total = 0
    for line in lines:
        first = next(c for c in line if c.isdigit())
        last = next(c for c in reversed(line) if c.isdigit())
        num = int(first + last)
        total += num
        
    print('Solution: {}'.format(total))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
