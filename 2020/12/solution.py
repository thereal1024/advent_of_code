#!/usr/bin/env python3

DIR = {'N': (0, 1), 'W': (-1, 0), 'S': (0, -1), 'E': (1, 0)}
import math

def solution(lines):
    x, y = 0.0, 0.0
    face_rad = 0
    for line in lines:
        cmd = line[0]
        amt = int(line[1:])
        if cmd in DIR:
            x, y = x + DIR[cmd][0] * amt, y + DIR[cmd][1] * amt
        elif cmd in ['L', 'R']:
            sign = 1 if cmd == 'L' else -1
            face_rad += sign * amt * math.pi / 180
            face_rad %= 2 * math.pi
        elif cmd == 'F':
            x, y = x + math.cos(face_rad) * amt, y + math.sin(face_rad) * amt
    manhattan = int(round(abs(x) + abs(y), 3))
    print(f"Solution: {manhattan}")
    
if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
