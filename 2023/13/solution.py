#!/usr/bin/env python3

def find_mirror(pattern):
    for i in range(len(pattern) - 1):
        sym = True
        for j in range(min(i+1, len(pattern)-i-1)):
            l, r = i-j, i+1+j
            if pattern[l] != pattern[r]:
                sym = False
                break
        if sym:
            return i+1
    return None

def solution(lines):
    patterns = [p.split('\n') for p in lines.removesuffix('\n').split('\n\n')]

    rcount, ccount = 0, 0
    for pattern in patterns:
        cpattern = list(zip(*pattern))
        r = find_mirror(pattern)
        c = find_mirror(cpattern)
        assert (r is None) != (c is None)
        if r is not None:
            rcount += r
        if c is not None:
            ccount += c
        
    total = rcount * 100 + ccount
    print('Solution: {}'.format(total))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = file_in.read()
    solution(lines)
