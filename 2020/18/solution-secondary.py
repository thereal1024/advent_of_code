#!/usr/bin/env python3

import string
import math

def parenparse(linepart):
    pl = 0
    for i, c in enumerate(linepart):
        if c == '(':
            pl += 1
        if c == ')':
            pl -= 1
        if pl <= 0:
            break
    if pl < 0:
        raise Exception('unbalanced parens')
    assert linepart[i+1] in '+*'
    return linepart[1:i], linepart[i+1], i+2

def calc(line):
    muls = []
    adds_temp = []
    start = 0
    line += '*'
    for i, c in enumerate(line):
        if i < start:
            continue
        if c not in string.digits:
            if c == '(':
                assert start == i
                subq, c, start_adv = parenparse(line[i:])
                start += start_adv
                num = calc(subq)
            else:
                num = int(line[start:i])
                start = i+1
            if c == '+':
                adds_temp.append(num)
            elif c == '*':
                adds_temp.append(num)
                muls.append(adds_temp)
                adds_temp = []
            else:
                raise Exception('bad char: ' + foundchar)
    
    return math.prod(sum(adds) for adds in muls)

def solution(lines):
    wstriplines = (line.replace(' ', '') for line in lines)
    total = sum(calc(line) for line in wstriplines)
    print(f"Solution: {total}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
