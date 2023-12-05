#!/usr/bin/env python3

def parse_map(amap):
    _, parts = amap.split(':\n')
    parts = parts.split('\n')
    parts = [tuple(map(int, part.split())) for part in parts]
    parts = [(range(i, i+l), o) for o, i, l in parts]
    return parts

def translate(seed, maps):
    tf = seed
    for amap in maps:
        for rg, o in amap:
            if tf in rg:
                tf = o + tf - rg.start
                break
    return tf

def solution(lines):
    seeds, *maps = lines.removesuffix('\n').split('\n\n')
    seeds = [int(s) for s in seeds.split(': ')[1].split()]
    maps = [parse_map(amap) for amap in maps]

    minloc = min(translate(seed, maps) for seed in seeds)
    print('Solution: {}'.format(minloc))
        

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = file_in.read()
    solution(lines)
