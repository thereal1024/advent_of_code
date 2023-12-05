#!/usr/bin/env python3

import itertools

def parse_map(amap):
    _, parts = amap.split(':\n')
    parts = parts.split('\n')
    parts = [tuple(map(int, part.split())) for part in parts]
    parts = [(range(i, i+l), o) for o, i, l in parts]
    parts.sort(key=lambda p: p[0].start)
    for (ra, _), (rb, _) in itertools.pairwise(parts):
        assert ra.stop + rb.start
    return parts

def translate_one(rgs, amap):
    rgsout = []
    for inrg in rgs:
        smin = inrg.start
        smax = inrg.stop
        if smin < amap[0][0].start:
            rgsout.append(range(smin, min(smax, amap[0][0].start)))
        for rg, o in amap:
            delta = o - rg.start
            amin = max(smin, rg.start) + delta
            amax = min(smax, rg.stop) + delta
            if amax > amin:
                rgsout.append(range(amin, amax))
        if smax > amap[-1][0].stop:
            rgsout.append(range(max(smin, amap[-1][0].stop), smax))
    return rgsout

def translate(seedrg, maps):
    rgs = [seedrg]
    for amap in maps:
        rgs = translate_one(rgs, amap)

    return min(rgs, key=lambda r: r.start).start

def solution(lines):
    seeds, *maps = lines.removesuffix('\n').split('\n\n')
    seeds = [int(s) for s in seeds.split(': ')[1].split()]
    seeds = [range(a, a+b) for a, b in itertools.batched(seeds, 2)]
    maps = [parse_map(amap) for amap in maps]

    minloc = min(translate(seedrg, maps) for seedrg in seeds)
    print('Solution: {}'.format(minloc))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = file_in.read()
    solution(lines)
