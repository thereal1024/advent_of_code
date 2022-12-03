#!/usr/bin/env python3

import string

def priority(item):
    return string.ascii_letters.index(item) + 1

def find_common(e1, e2, e3):
    common = set(e1).intersection(set(e2)).intersection(set(e3))
    return next(iter(common))

def solution(lines):
    common_items = (find_common(*es) for es in zip(*[lines, lines, lines]))
    priorities = (priority(item) for item in common_items)
    total = sum(priorities)
    print(f'Solution: {total}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
