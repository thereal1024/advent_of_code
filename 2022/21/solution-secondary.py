#!/usr/bin/env python3

import operator

ROOT = 'root'
HUMAN = 'humn'
OPMAP = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}
REVOPLE = {
    operator.add: operator.sub,
    operator.sub: operator.add,
    operator.mul: operator.floordiv,
    operator.floordiv: operator.mul
}
REVOPRE = {
    operator.add: (False, operator.sub),
    operator.sub: (True, operator.sub),
    operator.mul: (False, operator.floordiv),
    operator.floordiv: (True, operator.floordiv)
}

def parse_monkey(line):
    name, rest = line.split(': ')
    tok = rest.split(' ')
    res = {}
    if name == ROOT:
        res['eq'] = (tok[0], tok[2])
    elif name == HUMAN:
        res['ctrl'] = tuple()
    elif len(tok) == 1:
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
        v1 = calc_num(monkeys, n1)
        v2 = calc_num(monkeys, n2)
        if v1 is None or v2 is None:
            monkeys[name]['rev'] = tuple()    
            return None
        return op(v1, v2)
    elif 'ctrl' in lookup:
        monkeys[name]['rev'] = tuple()
        return None
    else:
        raise Exception(f'bad entry: {name} {lookup}')

def calc_rev(monkeys, name, target):
    lookup = monkeys[name]
    if 'val' in lookup:
        raise Exception('not expected to reverse val')
    elif 'op' in lookup:
        op, n1, n2 = lookup['op']
        if 'rev' in monkeys[n1]:
            other = calc_num(monkeys, n2)
            subtarget = REVOPLE[op](target, other)
            return calc_rev(monkeys, n1, subtarget)
        elif 'rev' in monkeys[n2]:
            other = calc_num(monkeys, n1)
            swap, rop = REVOPRE[op]
            if swap:
                target, other = other, target
            subtarget = rop(target, other)
            return calc_rev(monkeys, n2, subtarget)
        else:
            raise Exception('no rev in: {name} {lookup}')
    elif 'ctrl' in lookup:
        return target
    else:
        raise Exception(f'bad entry: {name} {lookup}')

def solution(lines):
    monkeys = dict(parse_monkey(line) for line in lines)

    rootmonkey = monkeys[ROOT]
    assert 'eq' in rootmonkey
    n1, n2 = rootmonkey['eq']
    v1 = calc_num(monkeys, n1)
    v2 = calc_num(monkeys, n2)
    if v1 is None:
        target = v2
        rev = n1
    elif v2 is None:
        target = v1
        rev = n2
    soln = calc_rev(monkeys, rev, target)
    print(f'Solution: {soln}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
