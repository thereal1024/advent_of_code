#!/usr/bin/env python3

from collections import namedtuple

def validate_line(line):
    req, pw = line.split(': ')
    indices, letter = req.split(' ')
    indices = (int(num) - 1 for num in indices.split('-'))
    return sum(pw[index] == letter for index in indices) == 1

def solution(lines):
    valid_pws = sum(validate_line(line) for line in lines)
    print(f"Solution: {valid_pws}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
