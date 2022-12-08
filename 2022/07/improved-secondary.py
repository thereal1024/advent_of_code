#!/usr/bin/env python3

FS_SIZE = 70000000
UNUSED_NEED = 30000000
MAX_USED = FS_SIZE - UNUSED_NEED

def dirsize(contents):
    size = 0
    for entry in contents:
        tok1, tok2 = entry.split(' ')
        if tok1 == 'dir':
            pass # do nothing
        else:
            size += int(tok1)
    return size

def findtotal(cmds, totals_list):
    total = 0
    for cmd in cmds:
        if cmd.startswith('cd '):
            cddir = cmd.removeprefix('cd ')
            if cddir == '/':
                raise Exception('unsupported return to root')
            elif cddir == '..':
                break
            else:
                total += findtotal(cmds, totals_list)
        elif cmd.startswith('ls'):
            contents = cmd.split('\n')[1:]
            total += dirsize(contents)
        else:
            raise Exception(f'bad command: {cmd}')
            
    totals_list.append(total)
    return total

def solution(cmds):
    cmds = iter(cmds)
    firstcmd = next(cmds)
    assert firstcmd == 'cd /'
    totals_list = []
    disk_total = findtotal(cmds, totals_list)
    min_delete = disk_total - MAX_USED
    total = min(total for total in totals_list if total >= min_delete)
    print(f'Solution: {total}')

if __name__ == '__main__':
    file_in = open('input.txt')
    cmds = file_in.read().removeprefix('$ ').removesuffix('\n').split('\n$ ')
    solution(cmds)
