#!/usr/bin/env python3

from collections import defaultdict

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


def segment_subset(target, test, reqlen, flip=False):
    if not len(target) == reqlen:
        return False
    if flip:
        target, test = test, target
    return test.issubset(target)

def decode_num(display):
    wires, disp = display
        
    wire_map = dict((LEN_MAP[len(wire)], wire) for wire in wires if len(wire) in LEN_MAP)

    wire_map[9] = next(wire for wire in wires if segment_subset(wire, wire_map[4], 6))
    wire_map[0] = next(wire for wire in wires if wire != wire_map[9] and segment_subset(wire, wire_map[1], 6))
    wire_map[6] = next(wire for wire in wires if wire not in (wire_map[9], wire_map[0]) and len(wire) == 6)
    wire_map[3] = next(wire for wire in wires if segment_subset(wire, wire_map[1], 5))
    wire_map[5] = next(wire for wire in wires if wire != wire_map[3] and segment_subset(wire, wire_map[6], 5, flip=True))
    wire_map[2] = next(wire for wire in wires if wire not in (wire_map[3], wire_map[5]) and len(wire) == 5)
    
    wire_map = dict((wire, digit) for digit, wire in wire_map.items())
    number = int(''.join(str(wire_map[digit]) for digit in disp))
    return number

def solution(lines):
    displays = (parse_display(line) for line in lines)
    count = sum(decode_num(display) for display in displays)
    print(f'Solution: {count}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
