#!/usr/bin/env python3

from collections import defaultdict

def compress(val, c):
    val += ord(c)
    val *= 17
    val %= 256
    return val
    
def hash(s):
    val = 0
    for c in s:
        val = compress(val, c)
    return val

def solution(lines):
    lines = list(lines)
    assert len(lines) == 1
    steps = lines[0].split(',')
    
    boxes = defaultdict(dict)
    for step in steps:
        if '=' in step:
            name, num = step.split('=')
            num = int(num)
            boxnum = hash(name)
            boxes[boxnum][name] = num
        elif '-' in step:
            name = step.removesuffix('-')
            boxnum = hash(name)
            if name in boxes[boxnum]:
                del boxes[boxnum][name]
    
    total = 0
    for boxnum, box in boxes.items():
        for slotnum, focus in enumerate(box.values()):
            focus = (boxnum + 1) * (slotnum + 1) * focus
            total += focus
    
    print(f'Solution: {total}')


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
