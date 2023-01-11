#!/usr/bin/env python3

# num segments -> number
LEN_MAP = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}

def parse_display(line):
    wires, disp = line.split(' | ')
    wires = tuple(map(frozenset, wires.split(' ')))
    disp = tuple(map(frozenset, disp.split(' ')))
    return wires, disp

# counts nums in len map
def count_certain_nums(display):
    wires, disp = display
    wire_map = dict((wire, LEN_MAP[len(wire)]) for wire in wires if len(wire) in LEN_MAP)
    count = sum(1 for digitwire in disp if digitwire in wire_map)
    return count

def solution(lines):
    displays = (parse_display(line) for line in lines)
    count = sum(count_certain_nums(display) for display in displays)
    print(f'Solution: {count}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
