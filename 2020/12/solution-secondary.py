#!/usr/bin/env python3

DIR = {'N': (0, 1), 'W': (-1, 0), 'S': (0, -1), 'E': (1, 0)}
import math

def solution(lines):
    x, y = 0.0, 0.0
    wx, wy = 10.0, 1.0
    for line in lines:
        cmd = line[0]
        amt = int(line[1:])
        if cmd in DIR:
            wx, wy = wx + DIR[cmd][0] * amt, wy + DIR[cmd][1] * amt
        elif cmd in ['L', 'R']:
            sign = 1 if cmd == 'L' else -1
            cwm = math.sqrt(wx**2 + wy**2)
            cwa = math.atan2(wy, wx)
            nwa = (cwa + sign * amt * math.pi / 180) % (2 * math.pi)
            wx, wy = cwm * math.cos(nwa), cwm * math.sin(nwa)
        elif cmd == 'F':
            x, y = x + wx * amt, y + wy * amt

    manhattan = int(round(abs(x) + abs(y), 3))
    print(f"Solution: {manhattan}")
    
if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
