#!/usr/bin/env python3

def parse_cmd(line):
    switch, rest = line.split(' ')
    switch = bool(['off', 'on'].index(switch))
    x, y, z = rest.split(',')
    x1, x2 = map(int, x.removeprefix('x=').split('..'))
    y1, y2 = map(int, y.removeprefix('y=').split('..'))
    z1, z2 = map(int, z.removeprefix('z=').split('..'))
    x2 += 1
    y2 += 1
    z2 += 1
    return switch, ((x1, x2), (y1, y2), (z1, z2))

def get_cube_size(cube):
    switch, ((x1, x2), (y1, y2), (z1, z2)) = cube
    sign = [-1, 1][switch]
    return sign * (z2-z1) * (y2-y1) * (x2-x1)

def find_intersection(cube_a, cube_b):
    aswitch, ((ax1, ax2), (ay1, ay2), (az1, az2)) = cube_a
    bswitch, ((bx1, bx2), (by1, by2), (bz1, bz2)) = cube_b
    
    x1, x2 = max(ax1, bx1), min(ax2, bx2)
    y1, y2 = max(ay1, by1), min(ay2, by2)
    z1, z2 = max(az1, bz1), min(az2, bz2)
    if not(x2 > x1 and y2 > y1 and z2 > z1):
        return None
    
    switch = not bswitch
    
    return switch, ((x1, x2), (y1, y2), (z1, z2))

def follow_cmds(cmds):
    cubes = []
    
    for cmd in cmds:
        intersections_pre = [find_intersection(cmd, cube) for cube in cubes]
        intersections = [ints for ints in intersections_pre if ints is not None]
        cubes.extend(intersections)
        if cmd[0]: # is on
            cubes.append(cmd)

    return sum(get_cube_size(cube) for cube in cubes)

def solution(lines):
    cmds = [parse_cmd(line) for line in lines]
    onct = follow_cmds(cmds)
    print(f'Solution: {onct}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
