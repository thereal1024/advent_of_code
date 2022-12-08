#!/usr/bin/env python3

LIMIT = 100000

def dirsize(contents):
    size = 0
    for entry in contents:
        tok1, tok2 = entry.split(' ')
        if tok1 == 'dir':
            pass # do nothing
        else:
            size += int(tok1)
    return size

def findtotal(cmds, limit):
    total = 0
    cond_total = 0
    for cmd in cmds:
        if cmd.startswith('cd '):
            cddir = cmd.removeprefix('cd ')
            if cddir == '/':
                raise Exception('unsupported return to root')
            elif cddir == '..':
                break
            else:
                st, sc = findtotal(cmds, limit)
                total += st
                cond_total += sc
        elif cmd.startswith('ls'):
            contents = cmd.split('\n')[1:]
            total += dirsize(contents)
        else:
            raise Exception(f'bad command: {cmd}')
            
    if total <= limit:
        cond_total += total
    return total, cond_total

def solution(cmds):
    cmds = iter(cmds)
    firstcmd = next(cmds)
    assert firstcmd == 'cd /'
    _, total = findtotal(cmds, LIMIT)
    print(f'Solution: {total}')

if __name__ == '__main__':
    file_in = open('input.txt')
    cmds = file_in.read().removeprefix('$ ').removesuffix('\n').split('\n$ ')
    solution(cmds)
