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

TARGET = 1000000000000

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

def shift_offsets(offsets, coord, vh):
    x, y = coord
    shifted = []
    for dx, dy in offsets:
        shft = (x+dx, y+dy-vh)
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
    jets = next(lines)
    
    shapes = [shape_offsets(shape) for shape in SHAPES]
    
    jetcycle = enumerate(itertools.cycle(jets))
    shape_pars = itertools.cycle(shapes)

    # +y is up +x is right
    grid = []
    stack_h = 0
    
    clearrows = 7
    vh = 0
    
    summary = []
    heights = dict()
    last_shape_count = 0
    
    for i, (shape, (sw, sh)) in enumerate(shape_pars):
        h = len(grid)
        pos = (LEFT_GAP, stack_h+TOP_GAP)
        
        ext = max(0, stack_h+clearrows-vh - len(grid))
        grid.extend([[0] * WIDTH for _ in range(ext)])
        
        while True:
            jn, jet = next(jetcycle)
            if jet == '<':
                posq = (max(0,pos[0]-1), pos[1])
            elif jet == '>':
                posq = (min(WIDTH-sw,pos[0]+1), pos[1])
            if posq != pos:
                if grid_free(grid, shift_offsets(shape, posq, vh)):
                    pos = posq
            posq = (pos[0], pos[1]-1) 
            if posq[1]-vh == -1 or not grid_free(grid, shift_offsets(shape, posq, vh)):
                rest_shape(grid, shift_offsets(shape, pos, vh))
                stack_h = max(stack_h, pos[1] + sh)
                break
            pos = posq
        
        # zero indexed
        heights[i] = stack_h
        # fully blocked line optimization
        if stack_h > 0 and all(grid[stack_h-vh-1]):
            delta_height = stack_h-vh
            grid = grid[delta_height:]
            vh = stack_h
            # cycle detection
            # if we have a flat floor, then cycle detect for the following
            # (delta_shape, delta_height, shape#n, jet#n)
            # once we have repeat values, the grid state loops and we just
            # extrapolate.
            delta_shape = i - last_shape_count
            last_shape_count = i
            shape_n = (i+1) % len(shapes)
            jet_n = (jn+1) % len(jets)
            state = (delta_shape, delta_height, shape_n, jet_n)
            if state not in summary:
                summary.append(state)
            else:
                start_i = summary.index(state)
                # extract the prefix and cycle totals
                pre_shape = sum(entry[0] for entry in summary[:start_i])
                pre_height = sum(entry[1] for entry in summary[:start_i])
                cycle_shape = sum(entry[0] for entry in summary[start_i:])
                cycle_height = sum(entry[1] for entry in summary[start_i:])
                
                # linear scaling
                align_shapes = TARGET - pre_shape
                cycles, extra = divmod(align_shapes, cycle_shape)
                # use zero indexed lookup with a count => -1 for index
                pre_and_post_height = heights[pre_shape + extra - 1]
                cycled_height = cycles * cycle_height
                target_height = cycled_height + pre_and_post_height
                print(f'Solution {target_height}')
                break

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
