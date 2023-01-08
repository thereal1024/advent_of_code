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
    
    all_ingreds = ingredcount.keys()
    allg_ingreds = set(allg for allgpos in allgmap.values() for allg in allgpos)
    noallgs = all_ingreds - allg_ingreds
    noallgs_appear = sum(ingredcount[allg] for allg in noallgs)
    print(f'Solution: {noallgs_appear}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
