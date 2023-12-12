#!/usr/bin/env python3

def possibilities(row):
    poss = ['']
    for c in row:
        if c == '?':
            poss = [r + ' ' for r in poss] + [r + '#' for r in poss]
        else:
            poss = [r + c for r in poss]
    return poss

def validate(row, spgs):
    return spgs == [len(w)for w in row.split()]

def solution(lines):
    total = 0
    for line in lines:
        row, spgs = line.split(' ')
        row = row.replace('.', ' ')
        spgs = list(map(int, spgs.split(',')))
        total += sum(validate(poss, spgs) for poss in possibilities(row))
    
    print('Solution: {}'.format(total))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
