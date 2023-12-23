#!/usr/bin/env python3

import heapq
import sys

sys.setrecursionlimit(4000)

DIRS = {
    'v': (1, 0),
    '^': (-1, 0),
    '>': (0, 1),
    '<': (0, -1),
}

def solution(lines):
    lines = list(lines)
    h, w = len(lines), len(lines[0])
    
    spaces = set()
    forced = {}
    
    start = 0, 1
    end = h-1, w-2
    
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c != '#':
                spaces.add((y, x))
            if c in DIRS:
                forced[(y, x)] = DIRS[c]

    assert start in spaces and end in spaces    
    
    def valid_moves(point, otherpoints):
        notherpts = frozenset(otherpoints | {point})
        if point in forced:
            direc = forced[point]
            newpoint = point[0] + direc[0], point[1] + direc[1]
            if newpoint in notherpts:
                return []
            return [(newpoint, notherpts)]
        moves = []
        for direc in DIRS.values():
            newpoint = point[0] + direc[0], point[1] + direc[1]
            if newpoint in spaces and newpoint not in notherpts:
                moves.append((newpoint, notherpts))
        return moves
    
    def longest_path(start, otherpoints=frozenset()):
        if start == end:
            return 0
        best = float('-inf')
        for newpoint, notherpts in valid_moves(start, otherpoints):
            best = max(best, longest_path(newpoint, notherpts) + 1)
        return best
    
    longest = longest_path(start)
    print(longest)

    
if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
