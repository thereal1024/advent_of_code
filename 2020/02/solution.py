#!/usr/bin/env python3

from collections import namedtuple

def validate_line(line):
    req, pw = line.split(': ')
    counts, letter = req.split(' ')
    lower_bound, upper_bound = (int(num) for num in counts.split('-'))
    return pw.count(letter) in range(lower_bound, upper_bound+1)

def solution(lines):
    valid_pws = sum(validate_line(line) for line in lines)
    print(f"Solution: {valid_pws}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
