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
    
    boxes = defaultdict(list)
    for step in steps:
        if '=' in step:
            name, num = step.split('=')
            num = int(num)
            boxnum = hash(name)
            found = False
            for i in range(len(boxes[boxnum])):
                if boxes[boxnum][i][0] == name:
                    boxes[boxnum][i] = name, num
                    found = True
                    break
            if not found:
                boxes[boxnum].append((name, num))
        elif '-' in step:
            name = step.removesuffix('-')
            boxnum = hash(name)
            for i in range(len(boxes[boxnum])):
                if boxes[boxnum][i][0] == name:
                    boxes[boxnum].pop(i)
                    break
    
    total = 0
    for boxnum, box in boxes.items():
        for slotnum, (_, focus) in enumerate(box):
            focus = (boxnum + 1) * (slotnum + 1) * focus
            total += focus
    
    print(f'Solution: {total}')


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
