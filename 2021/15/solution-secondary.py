#!/usr/bin/env python3

import heapq

OFFSETS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

MUL = 5
LIMIT = 9

def valid_offsets(p, h, w):
    y, x = p
    points = ((y+dy, x+dx) for dy, dx in OFFSETS)
    valid_points = ((y, x) for y, x in points if y in range(h) and x in range(w))
    return valid_points

def parse_map(lines):
    grid = []
    for line in lines:
        parsed = []
        for c in line:
            parsed.append(int(c))
        grid.append(parsed)
        
    h = len(grid)
    w = len(grid[0])
    
    wrap = lambda x: ((x-1) % LIMIT) + 1
    supergrid = [[wrap(grid[y%h][x%w] + y//h + x//w) for x in range(w*MUL)] for y in range(h*MUL)]
    return supergrid

def best_path(grid):
    h = len(grid)
    w = len(grid[0])
    
    start = (0, 0)
    end = (h-1, w-1)
    
    best = {(y,x): float('inf') for y in range(h) for x in range(w)}
    best[start] = 0
    visited = set()
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while len(queue) > 0:
        ldist, v = heapq.heappop(queue)
        
        if v in visited:
            continue
        visited.add(v)
        
        for adj in valid_offsets(v, h, w):
            test_dist = best[v] + grid[adj[0]][adj[1]]
            if adj not in visited and test_dist < best[adj]:
                best[adj] = test_dist
                heapq.heappush(queue, (test_dist, adj))

    return best[end]

def solution(lines):
    grid = parse_map(lines)
    best_path_cost = best_path(grid)
    print(f'Solution: {best_path_cost}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
