#!/usr/bin/env python3

from collections import defaultdict

def parse_line(line):
    line = line.removesuffix(')')
    ingreds, allgs = line.split(' (contains ')
    ingreds = ingreds.split(' ')
    allgs = allgs.split(', ')
    return ingreds, allgs

def solution(lines):
    foods = (parse_line(line) for line in lines)
    
    allgmap = {}
    ingredcount = defaultdict(int)
    for ingreds, allgs in foods:
        for ingred in ingreds:
            ingredcount[ingred] += 1
        for allg in allgs:
            if allg in allgmap:
                allgmap[allg] &= set(ingreds)
            else:
                allgmap[allg] = set(ingreds)
    
    done = {}
    while len(allgmap) > 0:
        orig, ingred = next((orig, ingreds) for orig, ingreds in allgmap.items() if len(ingreds) == 1)
        del allgmap[orig]
        done[orig] = next(iter(ingred))
        for allg in allgmap.keys():
            if allg != orig:
                allgmap[allg] -= ingred

    done = sorted(done.items())
    ingredlist = ','.join(ingred for _, ingred in done)
    print(f'Solution: {ingredlist}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
