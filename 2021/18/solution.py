#!/usr/bin/env python3

import ast

def parse_snum(line):
    return ast.literal_eval(line)

def rec_add_left(v, num):
    if type(v) == int:
        return v + num
    l, r = v
    return [rec_add_left(l, num), r]

def rec_add_right(v, num):
    if type(v) == int:
        return v + num
    l, r = v
    return [l, rec_add_right(r, num)]

def explode_snum(sn, depth=0):
    if type(sn) == int:
        return False, sn, 0, 0
    
    l, r = sn
    if depth >= 4:
        assert type(l) == type(r) == int
        return True, 0, l, r
    
    exp, l, fl, fr = explode_snum(l, depth+1)
    if exp:
        if fr != 0:
            r = rec_add_left(r, fr)
            fr = 0
    else:
        exp, r, fl, fr = explode_snum(r, depth+1)
        if exp:
            if fl != 0:
                l = rec_add_right(l, fl)
                fl = 0
                
    return exp, [l, r], fl, fr

def split_snum(sn):
    if type(sn) == int:
        if sn < 10:
            return False, sn
        b, ext = divmod(sn, 2)
        return True, [b, b+ext]
    l, r = sn
    sp, l = split_snum(l)
    if not sp:
        sp, r = split_snum(r)
    return sp, [l, r]

def reduce_snum(sn):
    while True:
        expl, sn, _, _ = explode_snum(sn)
        if expl:
            continue
        spl, sn = split_snum(sn)
        if spl:
            continue
        break
    return sn

def add_snums(n1, n2):
    res = [n1, n2]
    return reduce_snum(res)

def snum_mag(v):
    if type(v) == int:
        return v
    l, r = v
    return 3 * snum_mag(l) + 2 * snum_mag(r)

def solution(lines):
    snums = [parse_snum(line) for line in lines]
    sni = iter(snums)
    acc = next(sni)
    for snum in sni:
        acc = add_snums(acc, snum)
    finalmag = snum_mag(acc)
    print(f'Solution: {finalmag}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
