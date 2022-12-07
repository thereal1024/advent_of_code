#!/usr/bin/env python3

LOCALSIZE = '_$lc'
TOTALSIZE = '_$tl'

def dirsize(contents):
    size = 0
    for entry in contents:
        tok1, tok2 = entry.split(' ')
        if tok1 == 'dir':
            pass # do nothing
        else:
            size += int(tok1)
    return size

def findtotalsize(sizemap):
    total = sizemap[LOCALSIZE]
    for name, val in sizemap.items():
        if name in (LOCALSIZE, TOTALSIZE):
            continue
        total += findtotalsize(val)
    sizemap[TOTALSIZE] = total
    return total

def findsmalldirtotal(sizemap, cond):
    total = 0
    if cond(sizemap[TOTALSIZE]):
        total += sizemap[TOTALSIZE]
    for name, val in sizemap.items():
        if name in (LOCALSIZE, TOTALSIZE):
            continue
        total += findsmalldirtotal(val, cond)
    return total

def solution(cmds):
    sizemap = {}
    path = []
    cwd = sizemap
    for cmd in cmds:
        if cmd.startswith('cd '):
            cddir = cmd.removeprefix('cd ')
            if cddir == '/':
                path = []
                cwd = sizemap
            elif cddir == '..':
                cwd = path.pop()
            else:
                path.append(cwd)
                if cddir not in cwd:
                    cwd[cddir] = {}
                cwd = cwd[cddir]
        elif cmd.startswith('ls'):
            contents = cmd.split('\n')[1:]
            size = dirsize(contents)
            cwd[LOCALSIZE] = size
        else:
            raise Exception(f'bad command: {cmd}')
   
    findtotalsize(sizemap)
    total = findsmalldirtotal(sizemap, lambda x: x <= 100000)
    print(f'Solution: {total}')

if __name__ == '__main__':
    file_in = open('input.txt')
    cmds = file_in.read().removeprefix('$ ').removesuffix('\n').split('\n$ ')
    solution(cmds)
