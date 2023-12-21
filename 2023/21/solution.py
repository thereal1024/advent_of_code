#!/usr/bin/env python3

# dy, dx
# RLDU
DIRS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

STEPS = 64

def solution(lines):
    lines = list(lines)
    h, w = len(lines), len(lines[0])
    
    spaces = set()
    start = None
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c != '#':
                spaces.add((y, x))
            if c == 'S':
                assert start == None
                start = y, x
    
    def step(points):
        newpoints = set()
        for point in points:
            for dir in DIRS:
                newpoint = point[0] + dir[0], point[1] + dir[1]
                if newpoint in spaces:
                    newpoints.add(newpoint)
        return frozenset(newpoints)
    
    
    points = frozenset({start})
    for _ in range(STEPS):
        points= step(points)
        
    plots = len(points)
    print(f'Solution: {plots}')
    

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
