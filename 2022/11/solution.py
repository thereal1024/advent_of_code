#!/usr/bin/env python3

def parsemonkey(section):
    lines = section.split('\n')
    res = {}
    res['list'] = list(map(int, lines[1].removeprefix('  Starting items: ').split(', ')))
    expr = lines[2].removeprefix('  Operation: new = ')
    operand = -100000
    if expr == 'old + old':
        res['op'] = lambda x: x + x
    elif expr == 'old * old':
        res['op'] = lambda x: x * x    
    elif expr.startswith('old + '):
        operand = int(expr.removeprefix('old + '))
        res['op'] = lambda x: x + operand
    elif expr.startswith('old * '):
        operand = int(expr.removeprefix('old * '))
        res['op'] = lambda x: x * operand
        
    testmod = int(lines[3].removeprefix('  Test: divisible by '))
    res['test'] = lambda x: x % testmod == 0
    res['fwd'] = {
        True: int(lines[4].removeprefix('    If true: throw to monkey ')),
        False: int(lines[5].removeprefix('    If false: throw to monkey '))
    }
    res['ins'] = 0
    return res

def solution(sections):
    monkeys = [parsemonkey(section) for section in sections]
    
    for _ in range(20):
        for monkey in monkeys:
            items = monkey['list']
            monkey['list'] = []
            for item in items:
                item = monkey['op'](item)
                item = item // 3
                testresult = monkey['test'](item)
                fwd = monkey['fwd'][testresult]
                monkeys[fwd]['list'].append(item)
                monkey['ins'] += 1
                    
    inspections = [monkey['ins'] for monkey in monkeys]
    top1, top2 = sorted(inspections, reverse=True)[:2]
    print(f'Solution: {top1 * top2}')

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
