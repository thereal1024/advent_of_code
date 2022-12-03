#!/usr/bin/env python3

import string

def find_item(line):
    comp_len = len(line) // 2
    first, second = line[:comp_len], line[comp_len:]
    common = set(first).intersection(set(second))
    return next(iter(common))

def priority(item):
    return string.ascii_letters.index(item) + 1

def solution(lines):
    common_items = (find_item(line) for line in lines)
    priorities = (priority(item) for item in common_items)
    total = sum(priorities)
    print(f'Solution: {total}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
