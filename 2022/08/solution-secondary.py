#!/usr/bin/env python3

def visibility_score(grid, x, y):
    w = len(grid[0])
    h = len(grid)
    limit = grid[y][x]
    # right
    for xi in range(x+1, w):
        if grid[y][xi] >= limit:
            break
    right_count = xi - x
    
    # left
    for xi in range(x-1, -1, -1):
        if grid[y][xi] >= limit:
            break 
    left_count = x - xi
    
    # down
    for yi in range(y+1, h):
        if grid[yi][x] >= limit:
            break
    down_count = yi - y
    
    # up
    for yi in range(y-1, -1, -1):
        if grid[yi][x] >= limit:
            break
    up_count = y - yi
    
    score = right_count * left_count * down_count * up_count
    return score


def solution(lines):
    grid = [list(map(int, row)) for row in lines]
    w = len(grid[0])
    h = len(grid)
    
    best_score = max(visibility_score(grid, x, y) for y in range(1,h-1) for x in range(1,w-1))
    
    print(f'Solution: {best_score}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
