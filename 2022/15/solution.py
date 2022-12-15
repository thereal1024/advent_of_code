#!/usr/bin/env python3

ROW = 2000000

def parse_beacon(line):
    ss, bs = line.split(': ')
    ss = ss.removeprefix('Sensor at x=')
    sx, sy = map(int, ss.split(', y='))
    bs = bs.removeprefix('closest beacon is at x=')
    bx, by = map(int, bs.split(', y='))
    return (sx, sy), (bx, by)

def count_open_in_row(beacons, row):
    rowcover = set()
    rowbeacons = set()
    
    for (sx, sy), (bx, by) in beacons:
        md = abs(by-sy) + abs(bx-sx)
        delta = md - abs(row-sy)
        for clx in range(sx-delta, sx+delta+1):
            rowcover.add(clx)
        if by == row:
            rowbeacons.add(bx)

    return len(rowcover-rowbeacons)

def solution(lines):
    beacons = [parse_beacon(line) for line in lines]
    open_spaces = count_open_in_row(beacons, ROW)
    print(f'Solution: {open_spaces}')


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
