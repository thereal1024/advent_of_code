#!/usr/bin/env python3

NUMBERS = [
    ['zero', 0],
    ['one', 1],
    ['two', 2],
    ['three', 3],
    ['four', 4],
    ['five', 5],
    ['six', 6],
    ['seven', 7],
    ['eight', 8],
    ['nine', 9]
]

def check(line, pos):
    if line[pos].isdigit():
        return int(line[pos])
    for number, integer in NUMBERS:
        if line[pos:].startswith(number):
            return integer
    return None

def solution(lines):
    total = 0
    for line in lines:
        for i in range(len(line)):
            first = check(line, i)
            if first != None:
                break
        
        for i in reversed(range(len(line))):
            last = check(line, i)
            if last != None:
                break
        
        num = 10 * first + last
        print(num)
        total += num
        
    print('Solution: {}'.format(total))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
