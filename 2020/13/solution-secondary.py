#!/usr/bin/env python3

import math

def chinese_remainder(mods, remainders):
    total = 0
    prod = math.prod(mods)
    for mod, remainder in zip(mods, remainders):
        p = prod // mod
        total += remainder * pow(p, -1, mod) * p
    return total % prod

def solution(lines):
    lines = list(lines)
    bus_times = lines[1].split(',')
    
    mods = []
    remainders = []
    for i, bus_time in enumerate(bus_times):
        if bus_time == 'x':
            continue
        bus_time = int(bus_time)
        mods.append(bus_time)
        remainders.append(bus_time - i % bus_time)
    
    soln = chinese_remainder(mods, remainders)
    print(f"Solution: {soln}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
