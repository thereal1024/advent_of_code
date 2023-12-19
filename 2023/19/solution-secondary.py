#!/usr/bin/env python3

import math

VARS = 'xmas'
MAXV = 4000

def parse_cmd(cmd):
    if ':' in cmd:
        cond, jump = cmd.split(':')
        if '<' in cond:
            var, val = cond.split('<')
            val = int(val)
            assert var in VARS
            cond = '<', var, val
        elif '>' in cond:
            var, val = cond.split('>')
            val = int(val)
            assert var in VARS
            cond = '>', var, val
        else:
            raise Exception(f'bad cond {cond}')
        return cond, jump
    else:
        assert all(c.isalpha() for c in cmd)
        return cmd,

def parse_workflow(ws):
    name, cmds = ws.removesuffix('}').split('{')
    cmds = [parse_cmd(cmd) for cmd in cmds.split(',')]
    assert len(cmds[-1]) == 1 and type(cmds[-1][0]) == str
    return name, cmds

def split(crange, cond):
    sym, var, num = cond
    rr = crange[var]
    swap = False
    if sym == '>':
        num += 1
        swap = True
    breaknum = min(rr.stop, max(rr.start, num))
    pr = range(rr.start, breaknum)
    fr = range(breaknum, rr.stop)
    if len(pr) == 0:
        pr = range(0)
    if len(fr) == 0:
        fr = range(0)
    if swap:
        pr, fr = fr, pr
    prc = crange.copy()
    frc = crange.copy()
    prc[var] = pr
    frc[var] = fr
    return prc, frc

def solution(lines):
    workflows, _ = map(lambda p: p.split('\n'), lines.split('\n\n'))
    workflows = dict(parse_workflow(ws) for ws in workflows)
    assert 'in' in workflows
    
    def evaluate(crange, wfname='in', n=0):
        if wfname in ['A', 'R']:
            if wfname == 'A':
                return math.prod(len(v) for v in crange.values())
            else:
                return 0
        wfc = workflows[wfname][n]
        if len(wfc) == 1:
            return evaluate(crange, wfc[0])
        cond, cname = wfc
        crjump, crcont = split(crange, cond)
        return evaluate(crjump, cname) + evaluate(crcont, wfname, n+1)
    
    crange = {c: range(1, MAXV+1) for c in VARS}
    total = evaluate(crange)
    print(f'Solution: {total}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = file_in.read().removesuffix('\n')
    solution(lines)
