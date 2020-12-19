#!/usr/bin/env python3

def proc_rule(rule):
    rid, optl = rule.split(': ')
    rid = int(rid)
    if optl.startswith('"'):
        assert len(optl) == 3 and optl[-1] == '"'
        ch = optl[1]
        return rid, ch
    opts = optl.split(' | ')
    optidl = [list(map(int, opt.split(' '))) for opt in opts]
    return rid, optidl

def is_valid_count(rules, msg, rule_n, offset):
    optl = rules[rule_n]
    if type(optl) == str:
        return int(offset < len(msg) and msg[offset] == optl)
    for opt in optl:
        test_offset = offset
        valid_subrules = 0
        for rn in opt:
            adv = is_valid_count(rules, msg, rn, test_offset)
            if adv == 0:
                break
            test_offset += adv
            valid_subrules += 1
        if valid_subrules == len(opt):
            return test_offset - offset
    return 0

def is_valid(rules, msg):
    return is_valid_count(rules, msg, 0, 0) == len(msg)

def solution(sections):
    rules, msgs = sections
    rules = (rule.strip() for rule in rules.split('\n'))
    msgs = (msg.strip() for msg in msgs.split('\n') if msg)
    
    rules = dict(proc_rule(rule) for rule in rules)
    valid_msgs = sum(is_valid(rules, msg) for msg in msgs)
    print(f"Solution: {valid_msgs}")

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().split('\n\n')
    solution(sections)
