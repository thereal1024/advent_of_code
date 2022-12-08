#!/usr/bin/env python3

def solution(lines):
    grid = [list(map(int, row)) for row in lines]
    w = len(grid[0])
    h = len(grid)
    
    vis = [[False] * w for i in range(h)]
    
    # rows
    for yi in range(h):
        # left to right
        vis[yi][0] = True
        last = grid[yi][0]
        for xi in range(1, w):
            t = grid[yi][xi]
            if t > last:
                vis[yi][xi] = True
                last = t
        # right to left
        vis[yi][w-1] = True
        last = grid[yi][w-1]
        for xi in range(w-2, -1, -1):
            t = grid[yi][xi]
            if t > last:
                vis[yi][xi] = True
                last = t
    
    # cols
    for xi in range(w):
        # top to bottom
        vis[0][xi] = True
        last = grid[0][xi]
        for yi in range(1, h):
            t = grid[yi][xi]
            if t > last:
                vis[yi][xi] = True
                last = t
        # bottom to top
        vis[h-1][xi] = True
        last = grid[h-1][xi]
        for yi in range(h-2, -1, -1):
            t = grid[yi][xi]
            if t > last:
                vis[yi][xi] = True
                last = t
    
    visible = sum(sum(row) for row in vis)
    print(f'Solution: {visible}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
