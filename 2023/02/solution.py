#!/usr/bin/env python3

from collections import defaultdict

def parse_trial(trial):
    items = trial.split(', ')
    items = [item.split(' ') for item in items]
    items = {col: int(ct) for ct, col in items}
    items = defaultdict(int, items)
    return items

def is_valid(trials, req):
    for trial in trials:
        for col, maximum in req.items():
            if trial[col] > maximum:
                return False
    return True

REQ = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def solution(lines):
    total = 0
    for line in lines:
        gamenum, trials = line.split(': ')
        gamenum = int(gamenum.split(' ')[1])
        trials = [parse_trial(trial) for trial in trials.split('; ')]
        if is_valid(trials, REQ):
            total += gamenum

    print('Solution: {}'.format(total))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
