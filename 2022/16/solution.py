#!/usr/bin/env python3

TIME = 30

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

def solution(lines):
    valves = dict(parse_valve(line) for line in lines)

    soln = {
        ('AA', False, frozenset()): {
            'rel': 0,
            'rate': 0
        }
    }
    for t in range(TIME):
        soln_next = {}
        for (pos, opening, opened), stat in soln.items():
            statc = dict(stat)
            if opening:
                opened = opened.union([pos])
                statc['rate'] += valves[pos]['rate']
            statc['rel'] += statc['rate']
            if pos not in opened and valves[pos]['rate'] > 0:
                soln_next[(pos, True, opened)] = statc # open valve choice
            for nextpos in valves[pos]['conn']:
                key = (nextpos, False, opened)
                if key in soln_next and statc['rel'] <= soln_next[key]['rel']:
                    continue
                soln_next[key] = dict(statc)
        soln = soln_next
    best = max(val['rel'] for val in soln.values())
    print(f'Solution: {best}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
