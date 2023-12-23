#!/usr/bin/env python3

import heapq
import sys

from collections import defaultdict
sys.setrecursionlimit(9000)

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
    
    adjacency = defaultdict(set)
    for point in spaces:
        for direc in DIRS.values():
            newpoint = point[0] + direc[0], point[1] + direc[1]
            if newpoint in spaces:
                adjacency[point].add((1, newpoint))
    
    while True:
        bridge = defaultdict(set)
        bypass = set()
        for point, adjs in adjacency.items():
            if len(adjs) == 2:
                (lc, lp), (rc, rp) = adjs
                if rp not in bypass and lp not in bypass:
                    tc = lc + rc
                    bridge[lp].add((tc, rp))
                    bridge[rp].add((tc, lp))
                    bypass.add(point)
        newadj = defaultdict(set)
        for point, adjs in adjacency.items():
            if point not in bypass:
                for cost, adjpoint in adjs:
                    if adjpoint not in bypass:
                        newadj[point].add((cost, adjpoint))
        for point, adjs in bridge.items():
            newadj[point].update(adjs)
        
        if len(newadj) == len(adjacency):
            break
        adjacency = newadj
            
    assert start in adjacency and end in adjacency
    
    def valid_moves(point, otherpoints):
        notherpts = frozenset(otherpoints | {point})
        moves = []
        for cost, newpoint in adjacency[point]:
            if newpoint not in notherpts:
                moves.append((cost, newpoint, notherpts))
        return moves
    
    def longest_path(start, otherpoints=frozenset()):
        if start == end:
            return 0
        best = float('-inf')
        for cost, newpoint, notherpts in valid_moves(start, otherpoints):
            best = max(best, longest_path(newpoint, notherpts) + cost)
        return best
    
    longest = longest_path(start)
    print(longest)

    
if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
