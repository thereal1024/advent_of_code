#!/usr/bin/env python3

import math

OFFSETS = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def is_tree(treemap, x, y):
    width = len(treemap[0])
    x = x % width
    return treemap[y][x] == '#'

def tree_count(treemap, offset):
    x_offset, y_offset = offset
    out_vert = len(treemap)
    x, y = 0, 0
    trees_encountered = 0
    while y < out_vert:
        if is_tree(treemap, x, y):
            trees_encountered += 1
        x, y = x + x_offset, y + y_offset
    return trees_encountered
    
def solution(lines):
    treemap = list(lines)
    width = len(treemap[0])
    assert all(len(line) == width for line in treemap)
    product = math.prod(tree_count(treemap, offset) for offset in OFFSETS)
    print(f"Solution: {product}")
    

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
