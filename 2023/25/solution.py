#!/usr/bin/env python3

import random

def solution(lines):
    
    vertices = set()
    edges = set()
    for line in lines:
        key, vals = line.split(': ')
        vals = vals.split(' ')
        vertices.add(key)
        for val in vals:
            if (key, val) not in edges and (val, key) not in edges:
                edges.add((key, val))
                vertices.add(val)

    # Karger's algorithm. ~40-400 iterations on puzzle input.
    while True:
        aggregates = [{v} for v in vertices]
        remedges = list(edges)
        random.shuffle(remedges)
        
        def getaggs(l, r):
            li = next(i for i, agg in enumerate(aggregates) if l in agg)
            ri = next(i for i, agg in enumerate(aggregates) if r in agg)
            return li, ri
        
        while len(aggregates) > 2:
            edge = remedges.pop()
            lp, rp = edge
            laggi, raggi = getaggs(lp, rp)
            if laggi == raggi:
                continue
            lagg = aggregates[laggi]
            lagg.update(aggregates.pop(raggi))
        
        cuts = 0
        for lp, rp in remedges:
            laggi, raggi = getaggs(lp, rp)
            if laggi != raggi:
                cuts += 1
            
        if cuts == 3:
            break
    
    agg1, agg2 = aggregates
    ct1, ct2 = len(agg1), len(agg2)
    soln = ct1 * ct2
    print(f'Solution: {soln}')


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
