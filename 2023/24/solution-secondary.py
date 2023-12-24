#!/usr/bin/env python3

from sympy import symbols, Eq, solve

def solution(lines):
    hailstones = []
    for line in lines:
        pos, vel = line.split(' @ ')
        pos = tuple(map(int, pos.split(', ')))
        vel = tuple(map(int, vel.split(', ')))
        hailstones.append((pos, vel))

    tp = symbols('tp(x:z)')
    tv = symbols('tv(x:z)')
    tc = symbols('t(:3)')

    equations = []
    for (p, v), t in zip(hailstones, tc):
        for tpc, tvc, pc, vc in zip(tp, tv, p, v):
            equations.append(Eq(tpc + tvc * t, pc + vc * t))
            
    soln = solve(equations, *(tp + tv + tc))
    assert len(soln) == 1
    sumxyz = sum(soln[0][:3])
    print(f'Solution: {sumxyz}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
