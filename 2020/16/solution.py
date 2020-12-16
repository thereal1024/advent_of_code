#!/usr/bin/env python3

def parse_range(range_str):
    lb, ub = range_str.split('-')
    return range(int(lb), int(ub) + 1)

def parse_rule(rule):
    name, rule_pair = rule.split(': ')
    range1, range2 = rule_pair.split(' or ')
    range1, range2 = parse_range(range1), parse_range(range2)
    return (name, (range1, range2))

def parse_ticket(ticket):
    return [int(e) for e in ticket.split(',')]

def solution(sections):
    rules, my_ticket, nearby_tickets = sections
    rules = dict(parse_rule(rule) for rule in rules.split('\n'))
    my_ticket = parse_ticket(my_ticket.split('\n')[1])
    nearby_tickets = [parse_ticket(ticket) for ticket in nearby_tickets.rstrip().split('\n')[1:]]
    
    error_rate = 0
    for ticket in nearby_tickets:
        for value in ticket:
            if not any(value in rule[0] or value in rule[1] for rule in rules.values()):
                error_rate += value
    
    print(f"Solution: {error_rate}")

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().split('\n\n')
    solution(sections)
