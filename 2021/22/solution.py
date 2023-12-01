#!/usr/bin/env python3

LOW = -50
HIGH = 50

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

def clamp(p1, p2, l=LOW, h=HIGH+1):
    assert p1 <= p2
    p1 = min(max(p1, l), h)
    p2 = max(min(p2, h), l)
    return p1, p2

def follow_cmds(cmds):
    on = set()
    
    for sw_on, ((x1, x2), (y1, y2), (z1, z2)) in cmds:
        x1, x2 = clamp(x1, x2)
        y1, y2 = clamp(y1, y2)
        z1, z2 = clamp(z1, z2)
        
        for x in range(x1, x2):
            for y in range(y1, y2):
                for z in range(z1, z2):
                    p = x, y, z
                    if sw_on:
                        on.add(p)
                    elif p in on:
                        on.remove(p)
    
    return on

def solution(lines):
    cmds = [parse_cmd(line) for line in lines]
    on = follow_cmds(cmds)
    onct = len(on)
    print(f'Solution: {onct}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
