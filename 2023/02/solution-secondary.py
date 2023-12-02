#!/usr/bin/env python3

from collections import defaultdict

def parse_trial(trial):
    items = trial.split(', ')
    items = [item.split(' ') for item in items]
    items = {col: int(ct) for ct, col in items}
    items = defaultdict(int, items)
    return items

def power_set(trials):
    colmax = defaultdict(int)
    for trial in trials:
        for col, count in trial.items():
            if count > colmax[col]:
                colmax[col] = count
    prod = 1
    for col in COLS:
        prod *= colmax[col]
    return prod

COLS = set(['red', 'green', 'blue'])

def solution(lines):
    total = 0
    for line in lines:
        gamenum, trials = line.split(': ')
        gamenum = int(gamenum.split(' ')[1])
        trials = [parse_trial(trial) for trial in trials.split('; ')]
        total += power_set(trials)

    print('Solution: {}'.format(total))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
