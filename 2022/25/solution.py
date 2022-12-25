#!/usr/bin/env python3

import functools

SNAFU_REV = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2
}

SNAFU = {v: k for k, v in SNAFU_REV.items()}

def snafu_to_int(snafu):
    sum = 0
    for p, c in enumerate(reversed(snafu)):
        sum += SNAFU_REV[c] * 5**p
    return sum

@functools.cache
def bound_n(n):
    if n == 0:
        return 2
    cur = 2 * 5**n
    return cur + bound_n(n-1)


def int_to_snafu(num):
    p = 0
    while bound_n(p) < abs(num):
        p += 1

    out = ''
    while p >= 0:
        base = 5**p
        digit, num = divmod(num, base)
        if p > 0 and num > bound_n(p-1):
            digit += 1
            num -= base
        out += SNAFU[digit]
        p -= 1 
    assert num == 0
    return out


def solution(lines):
    fuels = (snafu_to_int(line) for line in lines)
    total_fuel = sum(fuels)
    snafu_total = int_to_snafu(total_fuel)
    print(f'Solution: {snafu_total}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
