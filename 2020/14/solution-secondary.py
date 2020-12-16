#!/usr/bin/env python3

from itertools import product
from functools import reduce

def unpack_mask(mask_str):
    vals = []
    for i, c in enumerate(reversed(mask_str)):
        if c == '0':
            continue
        elif c == '1':
            vals.append((0, 1 << i))
        else:
            raise Exception('not a bit: ' + c)
    return list(reversed(vals))

def solution(lines):
    mem = dict()
    floating_mask = None
    floating_and_mask = 2**32 - 1
    or_one_mask = 0
    for inst in lines:
        if inst.startswith('mask = '):
            arg = inst[7:]
            assert len(arg) == 36
            floating_mask = unpack_mask(arg.replace('1', '0').replace('X', '1'))
            floating_and_mask = int(arg.replace('0', '1').replace('X', '0'), 2)
            or_one_mask = int(arg.replace('X', '0'), 2)
        elif inst.startswith('mem['):
            addr, val = inst.split('] = ')
            addr = int(addr[4:])
            val = int(val)
            addr |= or_one_mask
            addr &= floating_and_mask
            for mask_i in product(*floating_mask):
                mask_i = reduce(lambda x, y: x | y, mask_i)
                mem[addr | mask_i] = val
        
    mem_sum = sum(mem.values())
    print(f"Solution: {mem_sum}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
