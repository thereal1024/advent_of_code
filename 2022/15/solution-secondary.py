#!/usr/bin/env python3

FRQ = 4000000
SEARCH = FRQ

def parse_beacon(line):
    ss, bs = line.split(': ')
    ss = ss.removeprefix('Sensor at x=')
    sx, sy = map(int, ss.split(', y='))
    bs = bs.removeprefix('closest beacon is at x=')
    bx, by = map(int, bs.split(', y='))
    return (sx, sy), (bx, by)

def merge_ranges(ranges, minv, maxv):
    out = []
    for begin, end in sorted(ranges):
        if out and out[-1][1] >= begin - 1:
            out[-1][1] = max(out[-1][1], end)
        else:
            out.append([begin, end])
    out = [(b, e) for b, e in out if e>=minv or b<=maxv]
    return out
        
def search_empty(beacons):
    soln = []
    for row in range(SEARCH):
        if row % 10000 == 0:
            print(f'Progress: on row {row} of {SEARCH}')
        coverranges = []
        for (sx, sy), (bx, by) in beacons:
            md = abs(by-sy) + abs(bx-sx)
            delta = md - abs(row-sy)
            rs, re = sx-delta, sx+delta
            if re >= rs:
                coverranges.append((rs, re))
        merged = merge_ranges(coverranges, 0, SEARCH)
        for m1, m2 in zip(*[merged, merged[1:]]):
            for x in range(m1[1]+1, m2[0]):
                soln.append((x,row))

    assert len(soln) == 1
    return soln[0]

def solution(lines):
    beacons = [parse_beacon(line) for line in lines]
    open_space = search_empty(beacons)
    code = open_space[0] * FRQ + open_space[1]
    print(f'Solution: {code}')


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
