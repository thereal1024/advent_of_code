#!/usr/bin/env python3

OFFSETS = [
    (0, 0, -1),
    (0, 0, 1),
    (0, -1, 0),
    (0, 1, 0),
    (-1, 0, 0),
    (1, 0, 0)
]

def surface_area(points):
    area = 0
    for point in points:
        for offset in OFFSETS:
            neighbor = (point[0]+offset[0], point[1]+offset[1], point[2]+offset[2])
            if neighbor not in points:
                area += 1
    return area

def parse_point(line):
    return tuple(map(int,line.split(',')))

def solution(lines):
    points = set(parse_point(line) for line in lines)
    area = surface_area(points)
    print(f'Solution: {area}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
