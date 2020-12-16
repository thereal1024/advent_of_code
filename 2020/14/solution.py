#!/usr/bin/env python3

def solution(lines):
    mem = dict()
    and_zero_mask = 2**36 - 1
    or_one_mask = 0
    for inst in lines:
        if inst.startswith('mask = '):
            arg = inst[7:]
            assert len(arg) == 36
            and_zero_mask = int(arg.replace('X', '1'), 2)
            or_one_mask = int(arg.replace('X', '0'), 2)
        elif inst.startswith('mem['):
            addr, val = inst.split('] = ')
            addr = int(addr[4:])
            val = int(val)
            mem[addr] = (val | or_one_mask) & and_zero_mask
        
    mem_sum = sum(mem.values())
    print(f"Solution: {mem_sum}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
