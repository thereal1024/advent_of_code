#!/usr/bin/env python3

def find_mirror(pattern, skip=None):
    for i in range(len(pattern) - 1):
        if i+1 == skip:
            continue
        sym = True
        for j in range(min(i+1, len(pattern)-i-1)):
            l, r = i-j, i+1+j
            if pattern[l] != pattern[r]:
                sym = False
                break
        if sym:
            return i+1
    return None

def alternates(pattern):
    alts = []
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            newp = pattern.copy()
            flipped = '#.'['.#'.index(newp[y][x])]
            newp[y] = newp[y][:x] + flipped + newp[y][x+1:]
            alts.append(newp)
    return alts
            
def mirror_code(pattern, skip=(None, None)):
    cpattern = list(zip(*pattern))
    r = find_mirror(pattern, skip[0])
    c = find_mirror(cpattern, skip[1])
    return r, c

def solution(lines):
    patterns = [p.split('\n') for p in lines.removesuffix('\n').split('\n\n')]

    rcount, ccount = 0, 0
    for pattern in patterns:
        mc = mirror_code(pattern)
        found = False
        for altp in alternates(pattern):
            altmc = mirror_code(altp, mc)
            if altmc != (None, None):
                found = True
                break
        assert found

        r, c = altmc
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
