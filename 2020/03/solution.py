#!/usr/bin/env python3

X_OFFSET = 3
Y_OFFSET = 1

def is_tree(treemap, x, y):
    width = len(treemap[0])
    x = x % width
    return treemap[y][x] == '#'

def solution(lines):
    treemap = list(lines)
    width = len(treemap[0])
    assert all(len(line) == width for line in treemap)
    out_vert = len(treemap)
    x, y = 0, 0
    trees_encountered = 0
    while y < out_vert:
        if is_tree(treemap, x, y):
            trees_encountered += 1
        x, y = x + X_OFFSET, y + Y_OFFSET
    print(f"Solution: {trees_encountered}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
