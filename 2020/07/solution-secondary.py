#!/usr/bin/env python3

from functools import lru_cache

def parse_contain(contain_str):
    if contain_str.endswith(' bag'):
        contain_str = contain_str[:-4]
    elif contain_str.endswith(' bags'):
        contain_str = contain_str[:-5]
    else:
        raise Exception('bad contains string')
    count, name = contain_str.split(' ', maxsplit=1)
    count = int(count)
    return count, name

def parse_rule(rule_str):
    bag_name, contains = rule_str.rstrip('.').split(' bags contain ', maxsplit=1)
    if contains == 'no other bags':
        contain_list = tuple()
    else:
        contain_list = tuple(parse_contain(s) for s in contains.split(', '))
    return bag_name, contain_list

def solution(lines):
    lines = list(lines)
    rules = dict({parse_rule(line) for line in lines})
    assert len(rules) == len(lines)
    
    @lru_cache(maxsize=len(rules))
    def contains_count(bag_type):
        items = rules[bag_type]
        return sum(count + count * contains_count(contained_type) for count, contained_type in items)
    
    total_count = contains_count('shiny gold')
    print(f"Solution: {total_count}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    lines = (line for line in lines if line)
    solution(lines)
