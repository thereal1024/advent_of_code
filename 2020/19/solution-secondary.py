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
    optl = rules[rule_n]
    if type(optl) == str:
        return set([1]) if offset < len(msg) and msg[offset] == optl else set()
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
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    valid_msgs = sum(is_valid(rules, msg) for msg in msgs)
    print(f"Solution: {valid_msgs}")

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().split('\n\n')
    solution(sections)
