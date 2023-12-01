#!/usr/bin/env python3

from collections import Counter
from itertools import pairwise

ROUNDS = 10

def parse_rules(lines):
    rules = {}
    for line in lines:
        lookup, ins = line.split(' -> ')
        rules[lookup] = ins
    return rules

def expand_poly(rules, poly):
    out = ''
    for a, b in pairwise(poly):
        out += a + rules[a+b]
    out += poly[-1]
    return out

def solution(sections):
    poly, rules = sections
    rules = parse_rules(rules.split('\n'))
    for _ in range(ROUNDS):
        poly = expand_poly(rules, poly)
    
    ctr = Counter(poly)
    (_, m), *_, (_, l) = ctr.most_common(len(ctr))
    soln = m - l
    print(f'Solution: {soln}')


if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
