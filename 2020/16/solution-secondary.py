#!/usr/bin/env python3

import math

def parse_range(range_str):
    lb, ub = range_str.split('-')
    return range(int(lb), int(ub) + 1)

def parse_rule(rule):
    name, rule_pair = rule.split(': ')
    range1, range2 = rule_pair.split(' or ')
    range1, range2 = parse_range(range1), parse_range(range2)
    return (name, (range1, range2))

def parse_ticket(ticket):
    ticket = [int(e) for e in ticket.split(',')]
    assert len(ticket) == 20
    return ticket

def solution(sections):
    rules, my_ticket, nearby_tickets = sections
    rules = dict(parse_rule(rule) for rule in rules.split('\n'))
    my_ticket = parse_ticket(my_ticket.split('\n')[1])
    nearby_tickets = [parse_ticket(ticket) for ticket in nearby_tickets.rstrip().split('\n')[1:]]
    
    bad_indices = []
    for i, ticket in enumerate(nearby_tickets):
        valid = True
        for value in ticket:
            if not any(value in rule[0] or value in rule[1] for rule in rules.values()):
                valid = False
                break
        if not valid:
            bad_indices.append(i)
    
    filtered_tickets = [ticket for i, ticket in enumerate(nearby_tickets) if i not in bad_indices]
    possible_rules = [set(rules.keys()) for i in range(20)]
    for ticket in filtered_tickets:
        for i, value in enumerate(ticket):
            for rule_name, rule_pair in rules.items():
                if value not in rule_pair[0] and value not in rule_pair[1]:
                    possible_rules[i].remove(rule_name)

    rank_idx = sorted(enumerate(len(rules) for rules in possible_rules), key=lambda tup: tup[1])
    for loc, _ in rank_idx:
        assert len(possible_rules[loc]) == 1
        rule_rm = next(iter(possible_rules[loc]))
        for i, rules in enumerate(possible_rules):
            if i != loc and rule_rm in rules:
                rules.remove(rule_rm)
                
    assert all(len(possible_rule) == 1 for possible_rule in possible_rules)
    found_rules = [next(iter(rule)) for rule in possible_rules]
    
    soln = math.prod(value for rule_name, value in zip(found_rules, my_ticket) if rule_name.startswith('departure'))
    print(f"Solution: {soln}")

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().split('\n\n')
    solution(sections)
