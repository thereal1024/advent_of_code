#!/usr/bin/env python3

import math
import sys

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

def valid_counts(rules, msg, rule_n, offset):
    if offset >= len(msg):
        return set()
    optl = rules[rule_n]
    if type(optl) == str:
        return set([1]) if msg[offset] == optl else set()
    accept_lens = set()
    for opt in optl:
        test_offsets = set([offset])
        for rn in opt:
            next_offsets = set()
            for test_offset in test_offsets:
                advs = valid_counts(rules, msg, rn, test_offset)
                next_offsets.update(test_offset + adv for adv in advs)
            test_offsets = next_offsets
        accept_lens.update(test_offset - offset for test_offset in test_offsets)
    return accept_lens

def is_valid(rules, msg):
    return len(msg) in valid_counts(rules, msg, 0, 0)

def solution(sections):
    rules, msgs = sections
    rules = (rule.strip() for rule in rules.split('\n'))
    msgs = [msg.strip() for msg in msgs.split('\n') if msg]
    
    rules = dict(proc_rule(rule) for rule in rules)
    # rule must match at least 1 character
    # e.g. expansion_max =  max(len(msg) for msg in msgs)
    # but we can make an assumption that it may be lower
    expansion_max = 8
    # fully accurate substitition "approximations"
    rules[8] = [[42] * i for i in range(1, expansion_max+1)]
    rules[11] = [[42] * i + [31] * i for i in range(1, math.ceil(expansion_max / 2)+1)]
    valid_msgs = sum(is_valid(rules, msg) for msg in msgs)
    print(f"Solution: {valid_msgs}")

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().split('\n\n')
    solution(sections)
