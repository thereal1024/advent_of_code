#!/usr/bin/env python3

import string

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
    if i == len(linepart) - 1:
        return linepart[1:i], None, ''
    assert linepart[i+1] in '+*'
    return linepart[1:i], linepart[i+1], linepart[i+2:]

def calc(line, cont=lambda n: n):
    if line[0] in string.digits:
        foundchar = None
        for i, c in enumerate(line):
            if c not in string.digits:
                foundchar = c
                break
        if not foundchar:
            return cont(int(line))
        num = int(line[:i])
        rest = line[i+1:]
    elif line[0] == '(':
        subq, foundchar, rest = parenparse(line)
        num = calc(subq)
        if not rest:
            return cont(num)
    else:
        raise Exception('not num ' + line)
    if foundchar == '+':
        return calc(rest, lambda n: cont(num) + n)
    elif foundchar == '*':
        return calc(rest, lambda n: cont(num) * n)
    else:
        raise Exception('bad char: ' + foundchar)
    

def solution(lines):
    wstriplines = (line.replace(' ', '') for line in lines)
    total = sum(calc(line) for line in wstriplines)
    print(f"Solution: {total}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
