#!/usr/bin/env python3

import itertools


s1 = [[1,1,1,1]]
s2 = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]
s3 = [
    [0, 0, 1],
    [0, 0, 1],
    [1, 1, 1]
]
s4 = [[1], [1], [1], [1]]
s5 = [[1,1], [1,1]]
SHAPES = [s1, s2, s3, s4, s5]

WIDTH = 7

COUNT = 2022

LEFT_GAP = 2
TOP_GAP = 3

def shape_offsets(shape):
    offsets = []
    w, h = (len(shape[0]), len(shape))
    # we work up from the bottom since +y is up +x is right
    for dy, row in enumerate(reversed(shape)):
        for dx, c in enumerate(row):
            if c == 1:
                offsets.append((dx, dy))
    return offsets, (w, h)

def shift_offsets(offsets, coord):
    x, y = coord
    shifted = []
    for dx, dy in offsets:
        shft = (x+dx, y+dy)
        shifted.append(shft)
    return shifted

def grid_free(grid, offsets):
    return all(grid[y][x] == 0 for x, y in offsets)

def rest_shape(grid, offsets):
    for x, y in offsets:
        grid[y][x] = 1

def print_grid(grid):
    for row in reversed(grid):
        print(''.join('.#'[p] for p in row))

def solution(lines):
    jet = next(lines)
    
    shapes = [shape_offsets(shape) for shape in SHAPES]
    
    jets = itertools.cycle(jet)
    shape_pars = itertools.islice(itertools.cycle(shapes), COUNT)
    
    # +y is up +x is right
    grid = []
    stack_h = 0
    
    clearrows = 7
    
    for i, (shape, (sw, sh)) in enumerate(shape_pars):
        h = len(grid)
        pos = (LEFT_GAP, stack_h+TOP_GAP)
        
        ext = max(0, stack_h+clearrows - len(grid))
        grid.extend([[0] * WIDTH for _ in range(ext)])
        
        while True:
            jet = next(jets)
            if jet == '<':
                posq = (max(0,pos[0]-1), pos[1])
            elif jet == '>':
                posq = (min(WIDTH-sw,pos[0]+1), pos[1])
            if posq != pos:
                if grid_free(grid, shift_offsets(shape, posq)):
                    pos = posq
            posq = (pos[0], pos[1]-1) 
            if posq[1] == -1 or not grid_free(grid, shift_offsets(shape, posq)):
                rest_shape(grid, shift_offsets(shape, pos))
                stack_h = max(stack_h, pos[1] + sh)
                break
            pos = posq

    print(f'Solution: {stack_h}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
