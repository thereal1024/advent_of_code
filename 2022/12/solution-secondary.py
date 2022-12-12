#!/usr/bin/env python3

import string

class Node:
    def __init__(self):
        self.visited = False
        self.dist = float('inf')
    
    def __repr__(self):
        return "Node:" + str(self.__dict__)


def find_start_end(grid):
    start = None
    end = None
    for y, row in enumerate(grid):
        if 'S' in row:
            start = (y, row.index('S'))
        if 'E' in row:
            end = (y, row.index('E'))
    return start, end

def find_lowest_node(nodes):
    index = None
    best = float('inf')
    for y, row in enumerate(nodes):
        for x, node in enumerate(row):
            if node.dist < best and not node.visited:
                index = (y, x)
                best = node.dist
    return index


def height_chr_to_num(htcr):
    if htcr == 'S':
        htcr = 'a'
    elif htcr == 'E':
        htcr = 'z'
    return string.ascii_lowercase.index(htcr)

def valid_neighbors(grid, idx):
    h = len(grid)
    w = len(grid[0])
    point_ht = height_chr_to_num(grid[idx[0]][idx[1]])
    neighbors_relcoords = [(1,0), (-1,0), (0,1), (0,-1)]
    neighbors = []
    for dy, dx in neighbors_relcoords:
        coord = (idx[0]+dy, idx[1]+dx)
        if coord[0] not in range(h) or coord[1] not in range(w):
            continue
        # *** reverse comparison for reverse travel
        if point_ht - height_chr_to_num(grid[coord[0]][coord[1]]) <= 1:
            neighbors.append(coord)
    return neighbors

def solution(lines):
    # y x
    grid = list(lines)
    h = len(grid)
    w = len(grid[0])
    # **** swap start and end for reverse travel
    end, start = find_start_end(grid)
    
    nodes = [[Node() for _ in range(w)] for _ in range(h)]
    startnode = nodes[start[0]][start[1]]
    startnode.dist = 0
    endnode = nodes[end[0]][end[1]]
    
    while True:
        nodeidx = find_lowest_node(nodes)
        if nodeidx is None:
            break
        nbrs = valid_neighbors(grid, nodeidx)
        cnode = nodes[nodeidx[0]][nodeidx[1]]
        for nbr in nbrs:
            nnode = nodes[nbr[0]][nbr[1]]
            if not nnode.visited:
                nnode.dist = cnode.dist + 1
        cnode.visited = True

    min_a = min(node.dist for y, row in enumerate(nodes) for x, node in enumerate(row) if grid[y][x] in ('a','S'))
    print(f'Solution: {min_a}')


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
