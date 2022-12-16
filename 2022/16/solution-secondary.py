#!/usr/bin/env python3

import itertools

TIME = 26

def parse_valve(line):
    info, con = line.split('; ')
    it = info.split(' ')
    ci = con.removeprefix('tunnels lead to valves ').removeprefix(
        'tunnel leads to valve ')
    conn = list(ci.split(', '))
    return it[1], {
        'rate': int(it[-1].removeprefix('rate=')),
        'conn': conn
    }


def search(valves, start, mask):
    soln = {
        (start, False, 0): {
            'rel': 0,
            'rate': 0
        }
    }
    for t in range(TIME):
        soln_next = {}
        for (pos, opening, opened), stat in soln.items():
            statc = dict(stat)
            if opening:
                opened |= pos
                statc['rate'] += valves[pos]['rate']
            statc['rel'] += statc['rate']
            if pos & opened == 0 and pos & mask != 0 and valves[pos]['rate'] > 0:
                soln_next[(pos, True, opened)] = statc # open valve choice
            for nextpos in valves[pos]['conn']:
                key = (nextpos, False, opened)
                if key in soln_next and statc['rel'] <= soln_next[key]['rel']:
                    continue
                soln_next[key] = dict(statc)
        soln = soln_next
    best = max(val['rel'] for val in soln.values())
    return best

def solution(lines):
    valves = sorted([parse_valve(line) for line in lines], key=lambda x: x[1]['rate'], reverse=True)
    vmap = dict((key, 2**i) for i, (key, val) in enumerate(valves))    
    valves = dict((vmap[k], {'rate': v['rate'], 'conn': list(map(vmap.get, v['conn']))}) for k, v in valves)
    maskm = min(k for k, v in valves.items() if v['rate'] == 0) - 1

    start = vmap['AA']
    best = -1
    # This solution is fairly slow.
    for mi in range(maskm+1):
        if mi % 16 == 0:
            print(f'working on {mi} of {maskm+1}')
        best = max(best, search(valves, start, mi) + search(valves, start, mi^maskm))
    print(f'Solution: {best}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
