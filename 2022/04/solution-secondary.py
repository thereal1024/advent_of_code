#!/usr/bin/env python3

def has_subrange(line):
    first, second = line.split(',')
    f1, f2 = map(int, first.split('-'))
    s1, s2, = map(int, second.split('-'))
    first_s = (f1 >= s1) and (f1 <= s2)
    second_s = (s1 >= f1) and (s1 <= f2)
    return first_s or second_s

def solution(lines):
    subranges = (has_subrange(line) for line in lines)
    total = sum(subranges)
    print(f'Solution: {total}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
