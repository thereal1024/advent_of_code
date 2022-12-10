#!/usr/bin/env python3

def solution(lines):
    
    cycle = 1
    x = 1
    
    signal_sum = 0
    
    def maybe_measure_signal():
        nonlocal signal_sum
        if cycle % 40 == 20 and cycle <= 220:
            signal_val = x * cycle
            signal_sum += signal_val
    
    for op in lines:
        if op == 'noop':
            maybe_measure_signal()
            cycle += 1
        elif op.startswith('addx'):
            incr = int(op.removeprefix('addx '))
            maybe_measure_signal()
            cycle += 1
            maybe_measure_signal()
            cycle += 1
            x += incr
        else:
            raise Exception(f'unknown op: {op}')
    
    print(f'Solution: {signal_sum}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
