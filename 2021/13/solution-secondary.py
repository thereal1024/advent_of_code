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
    
def render_grid(grid):
    minx = min(x for x, _ in grid)
    maxx = max(x for x, _ in grid)
    miny = min(y for _, y in grid)
    maxy = max(y for _, y in grid)
    
    h = maxy - miny + 1
    w = maxx - minx + 1
    
    agrid = [[False for _ in range(w)] for _ in range(h)]
    for x, y in grid:
        agrid[y-miny][x-minx] = True
        
    return '\n'.join(''.join(' #'[e] for e in row) for row in agrid)

def solution(sections):
    gridlines, instrlines = sections
    grid = parse_grid(gridlines.split('\n'))
    instr = parse_instr(instrlines.split('\n'))

    for inst in instr:
        grid = fold_grid(grid, inst)

    rendered = render_grid(grid)
    
    print(f'Solution: \n{rendered}')

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
