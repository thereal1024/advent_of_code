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
    xp, yp, zp = zip(*points)
    minx, maxx = min(xp) - 1, max(xp) + 1
    miny, maxy = min(yp) - 1, max(yp) + 1
    minz, maxz = min(zp) - 1, max(zp) + 1
    
    # point definitely not inside
    start = (minx, miny, minz)
    seen = set()
    queue = [start]
    area = 0
    while queue:
        point = queue.pop()
        if point in seen:
            continue
        seen.add(point)
        for offset in OFFSETS:
            neighbor = (point[0]+offset[0], point[1]+offset[1], point[2]+offset[2])
            if not (minx <= neighbor[0] <= maxx and
                    miny <= neighbor[1] <= maxy and
                    minz <= neighbor[2] <= maxz):
                continue
            if neighbor in points:
                area += 1
            else:
                queue.append(neighbor)

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
