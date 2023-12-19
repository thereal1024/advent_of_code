#!/usr/bin/env python3

VARS = 'xmas'

def parse_cmd(cmd):
    if ':' in cmd:
        cond, jump = cmd.split(':')
        if '<' in cond:
            var, val = cond.split('<')
            val = int(val)
            assert var in VARS
            cond = lambda pt: pt[var] < val
        elif '>' in cond:
            var, val = cond.split('>')
            val = int(val)
            assert var in VARS
            cond = lambda pt: pt[var] > val
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

def parse_var(vs):
    vn, vv = vs.split('=')
    vv = int(vv)
    return vn, vv

def parse_part(ps):
    ps = ps.removeprefix('{').removesuffix('}').split(',')
    part = dict(parse_var(vs) for vs in ps)
    assert set(VARS) == part.keys()
    return part


def solution(lines):
    workflows, parts = map(lambda p: p.split('\n'), lines.split('\n\n'))
    workflows = dict(parse_workflow(ws) for ws in workflows)
    parts = [parse_part(ps) for ps in parts]
    assert 'in' in workflows
    print(workflows, parts)

    def is_accepted(part):
        wfname = 'in'
        while wfname not in ['A', 'R']:
            wf = workflows[wfname]
            for wfc in wf:
                if len(wfc) == 1:
                    wfname = wfc[0]
                    break
                cond, cname = wfc
                if cond(part):
                    wfname = cname
                    break
        return wfname == 'A'
    
    total = sum(sum(part.values()) for part in parts if is_accepted(part))
    print(f'Solution: {total}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = file_in.read().removesuffix('\n')
    solution(lines)
