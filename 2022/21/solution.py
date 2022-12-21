#!/usr/bin/env python3

import operator

ROOT = 'root'
OPMAP = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}

def parse_monkey(line):
    name, rest = line.split(': ')
    tok = rest.split(' ')
    res = {}
    if len(tok) == 1:
        res['val'] = int(tok[0])
    elif len(tok) == 3:
        res['op'] = (OPMAP[tok[1]], tok[0], tok[2])
    else:
        raise Exception(f'bad line: {line}')
    return name, res


def calc_num(monkeys, name):
    lookup = monkeys[name]
    if 'val' in lookup:
        return lookup['val']
    elif 'op' in lookup:
        op, n1, n2 = lookup['op']
        return op(calc_num(monkeys, n1), calc_num(monkeys, n2))
    else:
        raise Exception(f'bad entry: {name} {lookup}')

def solution(lines):
    monkeys = dict(parse_monkey(line) for line in lines)
    soln = calc_num(monkeys, ROOT)
    print(f'Solution: {soln}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
