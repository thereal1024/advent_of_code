#!/usr/bin/env python3

from collections import defaultdict

START = 'start'
END = 'end'

def parse_map(lines):
    cave_map = defaultdict(tuple)
    for line in lines:
        a, b = line.split('-')
        cave_map[a] += b,
        cave_map[b] += a,
    assert START in cave_map and END in cave_map
    return cave_map

def find_path_count(cave_map):
    small_caves = set(p for p in cave_map if p.islower() and p not in (START, END))
    
    def path_count(path):
        nonlocal cave_map, small_caves
        adj = [p for p in cave_map[path[-1]] if p != START and (p not in small_caves or p not in path)]
        count = 0
        for p in adj:
            if p == END:
                count += 1
            else:
                count += path_count(path + (p,))
        return count
    
    return path_count((START,))

def solution(lines):
    cave_map = parse_map(lines)
    path_count = find_path_count(cave_map)
    print(f'Solution: {path_count}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
