#!/usr/bin/env python3

from collections import Counter, defaultdict
from itertools import pairwise

ROUNDS = 40

def parse_rules(lines):
    rules = {}
    for line in lines:
        lookup, ins = line.split(' -> ')
        rules[lookup] = ins
    return rules

def expand_poly(rules, poly):
    out = defaultdict(int)
    for code, ct in poly.items():
        s, e = code
        m = rules[code]
        out[s+m] += ct
        out[m+e] += ct
    return out

def flatten_poly(poly, polylast):
    out = Counter()
    for (a, _), ct in poly.items():
        out[a] += ct
    out[polylast] += 1
    return out

def solution(sections):
    poly, rules = sections
    rules = parse_rules(rules.split('\n'))
    
    polylast = poly[-1] # static last char
    poly = Counter(a+b for a, b in pairwise(poly))
    
    for _ in range(ROUNDS):
        poly = expand_poly(rules, poly)
    
    ctr = flatten_poly(poly, polylast)
    (_, m), *_, (_, l) = ctr.most_common(len(ctr))
    soln = m - l
    print(f'Solution: {soln}')


if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
