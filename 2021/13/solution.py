#!/usr/bin/env python3

def parse_grid(lines):
    grid = set()
    for line in lines:
        x, y = map(int, line.split(','))
        grid.add((x,y))
    return grid

def parse_instr(lines):
    instr = []
    for line in lines:
        eq = line.removeprefix('fold along ')
        d, n = eq.split('=')
        assert d in 'xy'
        n = int(n)
        instr.append((d, n))
    return instr

def fold_grid(grid, inst):
    dim, coord = inst
    
    if dim == 'x':
        fold = lambda x, y: ((x if x < coord else 2*coord - x), y)
    else:
        fold = lambda x, y: (x, (y if y < coord else 2*coord - y))
    
    newgrid = set()
    for x, y in grid:
        newgrid.add(fold(x, y))
    return newgrid
    

def solution(sections):
    gridlines, instrlines = sections
    grid = parse_grid(gridlines.split('\n'))
    instr = parse_instr(instrlines.split('\n'))

    grid = fold_grid(grid, instr[0])
    points = len(grid)
    print(f'Solution: {points}')

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
